let boxs = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset");

let turnO = true;

let winPatterns  = [
   [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
boxs.forEach((box) => {
    box.addEventListener("click", () => {
        if (turnO === true){
            box.innerHTML = "O";
            turnO = false;
        } else{
            box.innerHTML = "X";
            turnO = true;
        }
        box.disabled = true;
    });
});


