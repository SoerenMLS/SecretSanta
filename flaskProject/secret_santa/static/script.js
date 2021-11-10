let generate_invitation = async () => {
    let cookie = document.cookie.split('=')[1];
    let uidJson = JSON.stringify( {
        'userid': cookie
    });
    console.log(uidJson);

    await fetch('http://localhost:5000/generate',{
        headers:{
            'Content-Type':'application/json',
        },
        method: 'POST',
        body: uidJson,
        redirect: "follow"
    }).then(response => {
        if(response.redirected) {
            window.location.href = response.url;
        }
    })
}

