function copy(data) {
    /* Get the text field */
 let security = data
 console.log(security)
 var copyText = document.getElementById(security);

 /* Select the text field */
 copyText.select();
 copyText.setSelectionRange(0, 99999); /* For mobile devices */

 /* Copy the text inside the text field */
 document.execCommand("copy");

 /* Alert the copied text */
 alert("Copied the text: " + copyText.value);
}

// function copyToClipboard(textToCopy) {
//   var input = document.createElement("input");
//   document.body.appendChild(input);
//   input.value = textToCopy;
//   input.select();
//   document.execCommand("Copy");
//   input.remove();
// }

// function copyLastColumn(tr) {
//   copyToClipboard(tr.lastElementChild.innerHTML);
//   alert('copied to clipboard');
// }