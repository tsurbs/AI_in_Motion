var express = require('express');
var app = express();
var serv = require('http').Server(app);
const {spawn} = require('child_process');

app.get('/',function(req,res) {
	res.sendFile(__dirname + '/client/index.html');
});
app.use('/client',express.static(__dirname + '/client'));

app.set('port', process.env.PORT || 2000);
app.set('host', process.env.HOST || '0.0.0.0')
serv.listen(app.get('port'), app.get('host'), function(){
  console.log("Express server listening on port " + app.get('port')+"and host"+app.get('host'));
});

var USER_LIST = [];
var SOCKET_LIST = [];

function newuser(id){
	var self = {
		id:id,
		name:"empty",
		answer:"empty",
		number:String(Math.floor(Math.random()*10))
	}
	return self;
}

var io = require('socket.io')(serv,{});
io.sockets.on('connection', function(socket){
	var user = newuser(socket.id);
	socket.emit("newUser", user.number)
	socket.id = Math.random();
	SOCKET_LIST[socket.id] = socket;

	console.log(user)
	USER_LIST[socket.id] = user;

	socket.on("user_in", function(user_in){
		var dataToSend;
		console.log(user_in[0])
		// spawn new child process to call the python script
		const python = spawn('python3', ['AIComplete.py', user_in[0], user_in[1]]);
		// collect data from script
		python.stdout.on('data', function (data) {
			console.log('Pipe data from python script ...');
			dataToSend = data.toString();
			console.log("data0"+dataToSend)
			socket.emit("AI_resp", dataToSend)
			break;
		});
		// in close event we are sure that stream from child process is closed
		/*python.on('close', (code) => {
			console.log(`child process close all stdio with code ${code}`);
			console.log("data"+dataToSend)
		socket.emit("AI_resp", dataToSend)
		});*/
	})

	socket.on('disconnect', function(){
		console.log(USER_LIST[socket.id].name+", "+USER_LIST[socket.id].answer)
		delete SOCKET_LIST[socket.id];
		delete USER_LIST[socket.id];
	})

	socket.on('disconnect',function(){
		delete SOCKET_LIST[socket.id];
	})
});