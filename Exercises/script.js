// DOM Manipulation

document.addEventListener("DOMContentLoaded",
   function (event) {

      function sayHello(event) {

         console.log(event);

         this.textContent = "Said it!"
         var name = document.getElementById("name").value;
         var messsage = "<h2>Hello " + name + "!</h2>";
         // document.getElementById("content").textContent = messsage; 
         document.getElementById("content").innerHTML = messsage;

         if (name == "student") {
            var title =
               document
                  .querySelector("h1")
                  .textContent;
            title += " & Loving it! ";

            document
               .querySelector("h1")
               .textContent = title;
         }

         // event handles are functions that you handle 
         // in a specific cycle
      }
      document.querySelector("button")
         .addEventListener("click", sayHello);


      document.querySelector("body")
         .addEventListener("mousemove",
            function (event) {
               if(event.shiftKey == true) {
                  console.log("x: " + event.clientX);
                  console.log("y: " + event.clientY);
               }
  
            }
         );
   }
);








// console.log(document.getElementById("title"));




//  HTML doesn't need to have our
// event listeners



// document.querySelector("button").
// onclick = sayHello; 