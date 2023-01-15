// document.getElementById('blog_img').onchange = function(e) {
//     const file = e.target.files[0]
//     const reader = new FileReader()
    
//     if (file) {
//         reader.readAsDataURL(file)
//     }

//     reader.onload = function(revent) {
//         const pImg = document.getElementById('preview_img')
//         const result = revent.target.result
//         if (!Boolean(pImg)) {

//             const previewImgDiv = document.getElementById('preview_img')

//             const previewDeleteButton = document.createElement('button')
//             previewDeleteButton.className = 'btn btn-danger w-100 d-block'
//             previewDeleteButton.type = 'button'

//             previewDeleteButton.onclick = function(e) {
//                 parentElem.removeChild(document.getElementById('preview_img'))
//             }

//             const previewDeleteButtonIcon = document.createElement('span')
//             previewDeleteButtonIcon.className = 'bi bi-trash3-fill'
//             previewDeleteButtonIcon.style.paddingRight = '6px'

//             previewDeleteButton.appendChild(previewDeleteButtonIcon)
//             previewDeleteButton.appendChild(new Text('Delete cover image'))

//             const previewImg = document.createElement('img')
//             previewImg.src = result
//             previewImg.className = 'img-fluid'

//             previewImgDiv.appendChild(previewDeleteButton)
//             previewImgDiv.appendChild(previewImg)
//         } else {
//             pImg.src = result
//         }
//     }
// }