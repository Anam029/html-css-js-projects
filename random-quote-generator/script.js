let quotes = [
    "“Die with memories, not dreams” - “Unknown”",
    "“The best way to predict the future is to create it.” - Peter Drucker",
    "“The only way to do great work is to love what you do.” - Steve Jobs",
    "“Success is not final, failure is not fatal: It is the courage to continue that counts.” - Winston Churchill"
];


let button = document.querySelector("button");
button.addEventListener("click", function(){
    let randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    document.querySelector("#quote").textContent = randomQuote;
    console.log(document.querySelector("#quote").textContent);
})
