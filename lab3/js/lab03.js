// 1 
let inputNameFiller = "пример: Иванов";
let nameInput = document.getElementById("ename");
nameInput.value = inputNameFiller;

nameInput.onfocus = () => {
    if (nameInput.value == inputNameFiller){
        nameInput.value = "";
    }
}
nameInput.onblur = () => {
    if (nameInput.value.length == 0){
        nameInput.value = inputNameFiller;
    }
}

// 2
document.getElementById("confirm-id-btn").onclick = () => {
    let employeeId = parseInt(document.getElementById("eid").value);
    if (isNaN(employeeId)){
        alert("Необходимо ввести число!");
    }
}

// 3
for (let tr of document.getElementById("fl-tbody").childNodes){
    if (tr.nodeName === 'TR'){
        let td;
        for (let child of tr.childNodes){
            if (child.nodeName === 'TD'){
                td = child;
            }
        }
        for (let a of td.childNodes){
            if (a.nodeName === 'A'){
                a.onclick = () => {
                    if (confirm('Are you sure you want to delete this entry?')) {
                        tr.style.display = 'none'
                    } 
                    else {
                        // do nothing!
                    }
                }
            }
        }
    }
}

// 4

let nameButton = document.getElementById("ename-btn");
nameButton.onclick = () => {
    window.open("page01.html?input="+nameInput.value, "_blank");
}

console.log()