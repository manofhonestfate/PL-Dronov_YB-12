n=0
function change()
{
e1=document.getElementsByClassName('r')
e2=document.getElementById('b')
if(n==0)
{
for(var i=0; i<e1.length;i++){
e1[i].style.fontStyle="italic";}
e2.value="Убрать курсив";
n=1;
}
else
{
for(var i=0; i<e1.length;i++){
e1[i].style.fontStyle="normal";}
e2.value="Вернуть курсив";
n=0
}}

function yellow()
{
s=document.getElementsByClassName('w');
for(var i=0; i<s.length;i++){
t=s[i].innerHTML
g=i+1
s[i].innerHTML=g+'.'+t;
s[i].style.backgroundColor="yellow";
}}