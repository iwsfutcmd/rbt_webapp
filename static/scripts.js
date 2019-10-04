const rulebox = document.getElementById("rulebox");
const rulesetSelect = document.getElementById("ruleset-select");
const testTable = document.getElementById("test-table")
const rulesetId = document.getElementById("rulesetid");

const setRules = () => {
    let id = rulesetSelect.value;
    fetch("/rules?id=" + id).then(r => r.json().then(rules => rulebox.value = rules));
}
const addRow = () => {
    let row = testTable.insertRow();
    row.innerHTML = `
        <td><input type="text" value="-" name="teststrings"/></td>
        <td><input type="text" value="-" name="expecteds"/></td>
        <td> - </td>
    `
}
const download = (filename, text) => {
    let a = document.createElement("a");
    a.setAttribute("href", 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    a.setAttribute("download", filename);
    a.style.display = "none";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

const handleKeypress = event => {
    if (event.ctrlKey && event.key === "s") {
        download('ruleset.rbt', rulebox.value);
        event.preventDefault();
    } else if (event.code === "F5") {
        document.getElementById("rbt-webapp").submit();
        event.preventDefault();
    }
}

const registerRuleset = () => {
    let formData = new FormData();
    formData.append("id", rulesetId.value);
    formData.append("rules", rulebox.value);
    fetch("/register", {method: "POST", body: formData}).then(r => {
        if (!r.ok) {
            alert("Ruleset ID already exists.")
        } else {
            r.json().then(j => alert(j.ids + " registered."))
        }
    })
}