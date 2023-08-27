let updatebuttons = document.getElementsByClassName("update-shelf")
for(let i=0; i < updatebuttons.length; i++){
  updatebuttons[i].addEventListener('click', function(){
    let bookISBN = this.dataset.bookisbn
    let action = this.dataset.action
    console.log(bookISBN, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      updateuserorder(bookISBN, action);
    }
  })
}


function updateuserorder(bookISBN, action){
  console.log('user is logged in')
  let url = '/pages/updateitem/'

  fetch(url, { 
    method: 'POST',
    headers:{
      'content-type' : 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({bookISBN, action})
  })

  .then((Response) => {
    return Response.json()
  })
  .then((data) => {
    console.log(data)
  })
}