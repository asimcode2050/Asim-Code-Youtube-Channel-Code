const fileElement = document.getElementById('file');
const outElement = document.getElementById('output');
const nameElement = document.getElementById('imgname');
const typeElement = document.getElementById('imgtype');

function file_upload(){
    const file = this.files[0];
    const file_reader = new FileReader();
    file_reader.addEventListener('load', event => {
     const img = document.createElement('img');
     img.setAttribute('src',event.target.result);
     img.setAttribute('width','250');
     outElement.appendChild(img);
     const name = document.createTextNode(file.name);
     const type = document.createTextNode(file.type);
     nameElement.append(name);
     typeElement.appendChild(type);
    }

    );
    file_reader.readAsDataURL(file);
}
fileElement.addEventListener('change',file_upload,false);
