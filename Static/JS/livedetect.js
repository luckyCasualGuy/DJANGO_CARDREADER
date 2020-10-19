let csrfToken = $('#MainCard').data("token");
let defaultUrl = $('#ImageFeed').attr('src');
let mobileUrl =  $('#ImageFeed').data('url');
let urlError = false;

function fetchData(){
    $.ajax({
        url: document.URL,
        async: true,
        dataType: 'json',
        data:{
            csrfmiddlewaretoken: csrfToken,
        },
        type: 'post',
        success: function(responce){
            document.querySelector('pre').innerText = responce["text"];
            document.getElementById('Value').innerText = responce["Value"];

            let value = parseFloat(responce["Value"]);
            
            if(value < 0.5){
                document.getElementById('Value').classList.remove('badge-success');
                document.getElementById('Value').classList.add('badge-danger');
            }
            else{
                document.getElementById('Value').classList.add('badge-success');
                document.getElementById('Value').classList.remove('badge-danger');
            }
            
            urlError = responce["urlError"];
            console.log(urlError, "urlError");
        },
    });
}

class ButtonMode{
    mode = true;
    
    toggle(){
        this.mode = !this.mode;
        document.getElementById('ImageFeed').src = (this.mode)? defaultUrl:mobileUrl;
        document.getElementById('ChangeButton').innerHTML = (this.mode)? 'GO TO MOBILE FEED MODE':'GO TO WEBCAM FEED MODE';

        document.getElementById('Alert').style.display = 'none';
        document.getElementById('IP').removeAttribute('style');
    }

    change(){ 
        if(this.mode){
            if(!urlError){
                this.toggle();
            }else{
                document.getElementById('Alert').style.display = 'block';
                document.getElementById('IP').style.color = '#dc3545';
            }
        }else{
            this.toggle();
        }


    }
}

$(document).ready(function(){
    setInterval(fetchData, 1000);

    let button = new ButtonMode();
    $('#ChangeButton').click(function(event){
        console.log("Button click");
        button.change();
    });

    $('#IpSet').click(function(event){
        let value = document.getElementById('IpInput').value;

        $.ajax({
            url: mobileUrl,
            dataType: 'json',
            data:{
                csrfmiddlewaretoken: csrfToken,
                urlValue: value
            },
            type: 'post',
            success: function(responce){
                console.log();

                document.getElementById('IP').innerText = responce['setUrl'];
            }
        });
    });
});
