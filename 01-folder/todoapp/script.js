let input = document.querySelector("#input")
let button = document.querySelector("#button")
let list = document.querySelector("#list")
let deleteBtn = document.querySelector("#deleteBtn")
let li 
let tasks = ["gym", "learn js"]
button.addEventListener("click", function(){
        let inputValue = input.value
        if(input.value === ""){
            return
        }
        li = document.createElement("li")
        li.innerText = inputValue
        list.append(li)
        
        
        tasks.push(inputValue)
        localStorage.setItem("tasks", JSON.stringify(tasks))
        
        


})
deleteBtn.addEventListener("click", function(){
       if(li){
   li.remove()
       }
        
    
    
})
