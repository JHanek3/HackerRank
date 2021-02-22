// Task
// button id is btn
// button's initial text is 0, after each clicb the button must increment by 1
//  button's textlable is the js object's innerHTML property
// button has the following style properties
//  width of 96px
//  height of 46px
// font-size is 24px
// .js and .css files are in different directories so use the link tag to provide the CSS file path and the script tag to privde the JS file path

//html
// <!-- Enter your HTML code here -->
// <!DOCTYPE html>
// <html>
//     <head>
//         <meta charset="utf-8">
//         <title>Button</title>
//         <link rel="stylesheet" href="css/button.css" type="text/css">
//     </head>
//     <body>
//         <button id="btn" type="button">0</button>
//         <script src="js/button.js" type="text/javascript"></script>
//     </body>
// </html>

// css
// #btn {
//   width: 96px;
//   height: 48px;
//   font-size: 24px;
// }

//js
// document.addEventListener('DOMContentLoaded', () => {
//   const button = document.getElementById('btn');
  
//   button.addEventListener('click', (e) => {
//         const count = Number(e.currentTarget.innerText) + 1;
      
//         e.currentTarget.innerText = count;
//    });
// });
