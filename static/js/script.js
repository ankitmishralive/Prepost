
// from bs4 import *
// import requests


// print(image("crypto"))

 var newbg = document.getElementById("bg");
    var background = new Image();
    background.onload = function() {
        newbg.src = this.src;
    }

    folder = document.URL
    // domain = "https://prepost.onrender.com/"
    domain = "https://www.prepost.neuralberg.com/"
    // folder = folder.replace("http://127.0.0.1:5000/","")
    folder = folder.replace(domain,"")
    // console.log(folder)
  
    // background.src = `static/image/category/Category/${folder}/`+(Math.floor(Math.random()*(5))+1)+".jpg";
    background.src = `static/image/category/Category/${folder}/`+(Math.floor(Math.random()*(5))+1)+".jpg";
    // background.src = `static/image/`+(Math.floor(Math.random()*(8))+1)+".jpg";






function download() {
        var container = document.getElementById("container");
        html2canvas(container, {
            height: container.offsetHeight,
            width: container.offsetWidth
        }).then(canvas => {
            var a = document.createElement('a');
            a.href = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
            a.download = "YourPost.jpg";
            a.click();
        });
    }


function CopyText() {
        // Get the target element by ID
        var targetElement = document.getElementById('News');     
        // Create a temporary textarea element
        var tempTextArea = document.createElement('textarea');
        // Set the textarea value to the text content of the target element
        tempTextArea.value = targetElement.textContent;
        // Append the textarea to the document body
        document.body.appendChild(tempTextArea);
        // Select the text in the textarea
        tempTextArea.select();
        // Copy the selected text to the clipboard
        document.execCommand('copy');
        // Remove the temporary textarea
        document.body.removeChild(tempTextArea);
        // Optionally, display a notification or perform other actions
        swal("Copied!", "Copied to clipboard", "success");
      }
      
    

      var aText = new Array(
        "A Service for Social Media Handlers & Content  Seekers, Access Latest News in Real Time",
        );
        var iSpeed = 40; // time delay of print out
        var iIndex = 0; // start printing array at this posision
        var iArrLength = aText[0].length; // the length of the text array
        var iScrollAt = 20; // start scrolling up at this many lines
         
        var iTextPos = 0; // initialise text position
        var sContents = ''; // initialise contents variable
        var iRow; // initialise current row
         
        // function typewriter()
        // {
        //  sContents =  ' ';
        //  iRow = Math.max(0, iIndex-iScrollAt);
        //  var destination = document.getElementById("typedtext");
         
        //  while ( iRow < iIndex ) {
        //   sContents += aText[iRow++] + '<br />';
        //  }
        //  destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "|";
        //  if ( iTextPos++ == iArrLength ) {
        //   iTextPos = 0;
        //   iIndex++;
        //   if ( iIndex != aText.length ) {
        //    iArrLength = aText[iIndex].length;
        //    setTimeout("typewriter()", 500);
        //   }
        //  } else {
        //   setTimeout("typewriter()", iSpeed);
        //  }
        // }
        
        
        // typewriter()


        function typewriter() {
            sContents = ' ';
            iRow = Math.max(0, iIndex - iScrollAt);
            var destination = document.getElementById("typedtext");
          
            while (iRow < iIndex) {
              sContents += aText[iRow++] + '<br />';
            }
            destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "|";
            if (iTextPos++ == iArrLength) {
              if (iIndex == aText.length - 1) {
                // Reset the index and text position to restart the animation
                iIndex = 0;
                iTextPos = 0;
              } else {
                iIndex++;
              }
              iArrLength = aText[iIndex].length;
            }
            setTimeout(typewriter, iSpeed);
          }
          
          // Initial call to start the typewriter animation
          typewriter();
          
       