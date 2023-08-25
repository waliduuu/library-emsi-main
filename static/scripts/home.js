let updatebuttons = document.getElementsByClassName("update-shelf")
for(let i=0; i < updatebuttons.length; i++){
  updatebuttons[i].addEventListener('click', function(){
    let bookISBN = this.dataset.book
    let action = this.dataset.action
    console.log(bookISBN, action)
    console.log(user)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{console.log('sending data')}
  })
}