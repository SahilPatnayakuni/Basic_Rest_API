const mongoose = require('mongoose')

const Player = new mongoose.Schema({
	firstName: {type: String, default:''},
	lastName: {type: String, default:''},
	position: {type: String, default:''},
	age: {type: Number, default:0},
	team: {type: String, default:''},
	password: {type:String}
})

module.exports = mongoose.model('Player', Player)