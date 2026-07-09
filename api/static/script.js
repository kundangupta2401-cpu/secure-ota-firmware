async function callAPI(endpoint){

    const response = await fetch(endpoint,{
        method:"POST"
    });

    const data = await response.json();

    addLog(data.message);
}

function addLog(message){

    const logs = document.getElementById("logs");

    const lines = message.split("\n");

    lines.forEach(line => {

        if(line.trim() !== ""){

            const item = document.createElement("li");

            item.innerHTML = "✔ " + line;

            logs.prepend(item);

        }

    });

}


document
.getElementById("generateBtn")
.addEventListener("click",()=>{

    callAPI("/generate_keys");

});

document
.getElementById("signBtn")
.addEventListener("click",()=>{

    callAPI("/sign_firmware");

});
document
.getElementById("verifyBtn")
.addEventListener("click",()=>{

    callAPI("/verify_firmware");

});
document
.getElementById("installBtn")
.addEventListener("click",()=>{

    callAPI("/install_firmware");

});

document
.getElementById("uploadBtn")
.addEventListener("click", uploadFirmware);

async function uploadFirmware(){

    const fileInput = document.getElementById("firmwareFile");

    if(fileInput.files.length===0){

        alert("Select Firmware");

        return;
    }

    const formData=new FormData();

    formData.append("file",fileInput.files[0]);

    const response=await fetch("/upload_firmware",{

        method:"POST",

        body:formData

    });

    const data=await response.json();

    addLog(data.message);

}