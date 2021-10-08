// task1
function set_placeholder(event, val) {
    var target = event.target;
    target.placeholder = val;

}
// task2
function check_num(){
    num = document.getElementsByName("num")[0].value;
    if (!parseInt(num)){
        alert('Введите цифры')
    }
}
// task3
for (let tr of document.getElementById("table-body").childNodes){
    if (tr.nodeName === 'TR'){

        let td;
        for (let child of tr.childNodes){

            if (child.nodeName === 'TH'){
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

let nameButton = document.getElementById("name-btn");

nameButton.onclick = () => {

    window.open("form.html?input="+nameInput.value, "_blank");
}

console.log()

