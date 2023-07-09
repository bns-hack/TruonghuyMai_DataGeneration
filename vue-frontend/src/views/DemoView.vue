
<template>
  <main>
<div class="endpoint-edit">
  <p class="title">Current Endpoint API URL : </p><p class="title2">{{endpoint}}</p> 
  <input v-model="endpoint" placeholder="edit me" />
</div>

  <div class="file-upload">
    <input class="title" accept=".csv"  type="file" @change="onFileChange" />
    <div v-if="progress" class="progess-bar" :style="{'width': progress}">{{progress}}</div>
    <button v-if="this.received" @click="onUploadFile" class="upload-button" :disabled="!this.selectedFile">Generate New Data</button>
    <div v-if="!this.received" class="lds-dual-ring"> Generating</div>


  </div>

  
  <div class="file-download">

  <span class="title" >Result Synthesize Data is Here:</span>
  <p style="white-space: pre-line;">{{ message }}</p>
  <textarea  id="myTextArea" cols=50 rows=15 disabled v-model="this.data" placeholder=""></textarea>

    <button :disabled="!this.finish" @click="downloadJSON" class="upload-button" >Download JSON</button>

  </div>
  </main>
</template>

<script>
  import axios from "axios";
  import { ref } from 'vue'
  

  const message = ref('')
  /* eslint-disable */
  export default {
      data() {
          return {
              selectedFile: "",
              progress: 0,
              data: "",
              filename:"",
              finish:"",
              endpoint:"http://127.0.0.1:5000",
              received:true
          };
      },
      methods: {
          onFileChange(e) {
              const selectedFile = e.target.files[0]; // accessing file
              this.selectedFile = selectedFile;
              this.progress = 0;
          },
          prettyPrint(data) {
              let ugly = data
              let obj = JSON.parse(ugly);
              let pretty = JSON.stringify(obj, undefined, 4);
              //document.getElementById('myTextArea').value = pretty;
              return pretty
          },
          onUploadFile() {
              const formData = new FormData();
              formData.append("file", this.selectedFile); // appending file
              this.received = false;
              console.log(this.received)

              const customHeader = {
                  headers: {
                  // Authorization: `Bearer ${getLocalStorageToken()}`,
                  "Access-Control-Allow-Origin": "*",
                  "Content-Type": 'multipart/form-data',
                  },
              };
              // sending file to backend
              axios
              .post( this.endpoint+"/upload", formData, customHeader,{
                  onUploadProgress: ProgressEvent => {
                  let progress =
                      Math.round((ProgressEvent.loaded / ProgressEvent.total) * 100) +
                      "%";
                  this.progress = progress;
                  }
              })
              .then(res => {
                  console.log(res);
                  this.data = this.prettyPrint(res.data)
                  //prettyPrint(this.data)
                  this.finish = true;
                  this.received = true;
              })
              .catch(err => {
                  console.log(err);
                  this.data = "CONNECTION ERROR"
                  //console.log(this.data)
                  this.finish = false;
              });
          },
          downloadCSV(){
              console.log(this.data + "JSON")
              let text = this.data;
              let filename = 'cats.csv';
              let element = document.createElement('a');
              element.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(text));
              element.setAttribute('download', filename);

              element.style.display = 'none';
              document.body.appendChild(element);

              element.click();
              document.body.removeChild(element); 
           
          },
          downloadJSON(){
              console.log(this.data + "JSON")
              let text = JSON.stringify(this.data);
              let filename = 'result.json';
              let element = document.createElement('a');
              element.setAttribute('href', 'data:application/json;charset=utf-8,' + encodeURIComponent(text));
              element.setAttribute('download', filename);

              element.style.display = 'none';
              document.body.appendChild(element);

              element.click();
              document.body.removeChild(element); 


          }  
         

      }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.file-upload {
  box-shadow: 2px 2px 9px 2px #ccc;
  border-radius: 1rem;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 1rem;
  width: 60%;
  margin: 0 auto;
  margin-top: 2rem;

}

.endpoint-edit {
  box-shadow: 2px 2px 9px 2px #ccc;
  border-radius: 1rem;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 1rem;
  width: 60%;
  margin: 0 auto;

}

.file-download {
  box-shadow: 2px 2px 9px 2px #ccc;
  border-radius: 1rem;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 1rem;
  width: 60%;
  margin: 0 auto;
  margin-top: 2rem;

}

.title{
  font-family: var(--pure-material-font, "Roboto", "Segoe UI", BlinkMacSystemFont, system-ui, -apple-system);
  font-size: 18px;
  font-weight: 500;

}

.title{
  font-family: var(--pure-material-font, "Roboto", "Segoe UI", BlinkMacSystemFont, system-ui, -apple-system);
  font-size: 18px;
  font-weight: 500;

}
input {
  font-size: 0.9rem;
}

input,
div,
button {
  margin-top: 2rem;
}

.progess-bar {
  height: 1rem;
  width: 0%;
  background-color: #151618;
  color: white;
  padding: 2px;
  font-weight: bold;
}

.upload-button {
  position: relative;
  display: inline-block;
  box-sizing: border-box;
  border: none;
  border-radius: 4px;
  padding: 0 16px;
  min-width: 64px;
  height: 36px;
  vertical-align: middle;
  text-align: center;
  text-overflow: ellipsis;
  text-transform: uppercase;
  color: rgb(var(--pure-material-onprimary-rgb, 255, 255, 255));
  background-color: #41b883;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12);
  font-family: var(--pure-material-font, "Roboto", "Segoe UI", BlinkMacSystemFont, system-ui, -apple-system);
  font-size: 14px;
  font-weight: 500;
  line-height: 36px;
  overflow: hidden;
  outline: none;
  cursor: pointer;
  transition: box-shadow 0.2s;
}

.upload-button::-moz-focus-inner {
  border: none;
}

/* Overlay */
.upload-button::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0;
  transition: opacity 0.2s;
}

/* Ripple */
.upload-button::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  border-radius: 50%;
  padding: 50%;
  width: 32px; /* Safari */
  height: 32px; /* Safari */
  background-color: rgb(var(--pure-material-onprimary-rgb, 255, 255, 255));
  opacity: 0;
  transform: translate(-50%, -50%) scale(1);
  transition: opacity 1s, transform 0.5s;
}

/* Hover, Focus */
.upload-button:hover,
.upload-button:focus {
  box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
}

.upload-button:hover::before {
  opacity: 0.08;
}

.upload-button:focus::before {
  opacity: 0.24;
}

.upload-button:hover:focus::before {
  opacity: 0.3;
}

/* Active */
.upload-button:active {
  box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2), 0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12);
}

.upload-button:active::after {
  opacity: 0.32;
  transform: translate(-50%, -50%) scale(0);
  transition: transform 0s;
}

/* Disabled */
.upload-button:disabled {
  color: rgba(var(--pure-material-onsurface-rgb, 0, 0, 0), 0.38);
  background-color: rgba(var(--pure-material-onsurface-rgb, 0, 0, 0), 0.12);
  box-shadow: none;
  cursor: initial;
}

.upload-button:disabled::before {
  opacity: 0;
}

.upload-button:disabled::after {
  opacity: 0;
}

.upload-button:disabled {
  background-color: #b3bcc4;
  cursor: no-drop;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
  font-family: var(--pure-material-font, "Roboto", "Segoe UI", BlinkMacSystemFont, system-ui, -apple-system);
  font-size: 14px;
  font-weight: 500;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #151618;
  border-color: #151618 transparent #151618 transparent;
  animation: lds-dual-ring 1.2s linear infinite;

}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}


@media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
</style>


