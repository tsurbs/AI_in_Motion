const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {
    var user_in = "hello"
    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['script.py', user_in]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        console.log(dataToSend)
        res.send(dataToSend)
    });
    
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))