import sys
from sanic import Sanic
from sanic.response import json, html, text
from jinja2 import Template
from utils import *

app = Sanic()


@app.route("/", methods=["GET", "POST"])
async def test(request):
    rbts = available_rbts()
    try:
        teststrings, expecteds = process_testdata(
            request.files["testdata"][0].body.decode("UTF-8"))
    except (ValueError, KeyError) as e:
        try:
            teststrings = request.form["teststrings"]
            expecteds = request.form["expecteds"]
        except KeyError:
            teststrings = ["-"]
            expecteds = ["-"]
    try:
        rules = request.files["rulefile"][0].body.decode("UTF-8")
        if not rules:
            raise ValueError
    except (ValueError, KeyError) as e:
        try:
            rules = request.form["rules"][0]
        except KeyError:
            rules = ""
    reverse = "reverse" in request.form
    try:
        rulesetname = request.form["rulesetname"][0]
    except KeyError:
        rulesetname = ""
    try:
        outputs = transliterate(rules, teststrings, reverse)
        error = ""
    except ValueError as e:
        outputs = [""] * len(teststrings)
        error = e
    testdata = zip(teststrings, expecteds, outputs)
    template = Template(open("template.jinja2").read())
    return html(template.render(
        rbts=rbts,
        rules=rules,
        rulesetname=rulesetname,
        testdata=testdata,
        error=error,
        reverse=reverse
    ))


@app.route("/rules")
async def rules(request):
    rules = get_rules(request.args["id"][0])
    return json(rules)

@app.post("/register")
async def register(request):
    ruleset_id = request.form["id"][0]
    try:
        registered_ids = register_ruleset(ruleset_id, request.form["rules"][0])
        return json({"ids": registered_ids}, status=201)
    except ValueError:
        return json({"ids": []}, status=400)

app.static("/static", "./static")

if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except (IndexError, ValueError) as e:
        host = "0.0.0.0"
        port = 8000
    app.run(host=host, port=port)
