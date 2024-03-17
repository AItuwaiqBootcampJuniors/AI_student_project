const path = require('path')
const express = require('express')
const database = require('mime-db')
const server = express()
server.use(express.json())
server.listen(80)


server.get('',function(req,res){
    res.sendFile(path.join(__dirname,'../Frontend','/form.html'))
})

server.post('/check',function(req,res){
    console.log(req.body)
    let gender = Number(req.body['Gender'])
    let age = Number(req.body['Age'])
    let em = Number(req.body['Married'])
    let agl = Number(req.body['AGL'])
    let bmi = Number(req.body['BMI'])
    let spawn_ai_app = require('child_process').spawn('python',['AI.py',gender,age,em,agl,bmi],{cwd:path.join(__dirname,'../AI')})
    spawn_ai_app.stdout.on('data',function(data){
        console.log(data.toString())
        if(Number(data.toString()) == 1){
            res.send({message:true})
        }else{
            res.send({message:false})
        }
    })
})

