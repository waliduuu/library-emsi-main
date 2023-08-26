let updatebuttons = document.getElementsByClassName("update-shelf")
for(let i=0; i < updatebuttons.length; i++){
  updatebuttons[i].addEventListener('click', function(){
    let bookISBN = this.dataset.book
    let action = this.dataset.action
    console.log(bookISBN, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      console.log('user is logged');
      updateuserorder(bookISBN, action);
    }
  })
}

function updateuserorder(bookISBN, action){
  let url = '/pages/updateitem/'
  fetch(url, {
    method: 'POST',
    headers:{
      'Content-Type' : 'application/json',
      'X-CSRFTOKEN': csrftoken,
    },
    body:JSON.stringify({'bookISBN': bookISBN, 'action': action})
  })
  .then((Response) =>{
    return Response.json()
  })
  .then((data) =>{
    console.log(data)
  })

}