let generate_invitation = async () => {
    let cookie = document.cookie.split('=');

    await fetch('http://localhost:5000/generate',{
        headers:{
            'Content-Type':'application/json',
        },
        method: 'POST',
        body: {
            userid: JSON.stringify(cookie[1]),
        },
        redirect: "follow"
    }).then(response => {
        if(response.redirected) {
            window.location.href = response.url;
        }
    })
}

