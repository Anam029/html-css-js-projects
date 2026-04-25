let cells = document.querySelectorAll(".col")
cells.forEach(function(cell){
    cell.addEventListener("click", function(dets){
        console.dir(dets);
    })
});