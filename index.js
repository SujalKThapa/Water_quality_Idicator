const express = require('express');
const app = express();
const path =require('path');

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static("public"));
app.set('views',path.join(__dirname,'views'));
app.set('view engine','ejs');

app.get('/form',(req,res)=>{
    res.render('form');
})


app.listen(3000, ()=>{
    console.log("On port 3000");
})