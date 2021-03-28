var audio = document.getElementById('audio');
var totalProgress = $('.totalProgress');
var totalTime = $('.total_time');
var currentProgress = $('.currentProgress');
var currentTime = $('.current_time');
var sb = 0;

window.onload = function(){
    totalTime.text(formatTime(audio.duration));
    $('.play').css({'display':'inline-block'});
    $('.pause').css({'display':'none'});
};
// 播放暂停切换
function play_song() {
    if(audio.paused){
        audio.play();
        $('.play').css({'display':'none'});
        $('.pause').css({'display':'inline-block'});
    }else{
       audio.pause();
        $('.play').css({'display':'inline-block'});
        $('.pause').css({'display':'none'});
    }
}
// 点击播放
$('.song').on('click', function () {
    play_song();
});
// 获取播放进度
totalProgress.on('click', function (ev) {
    var ratio = getRatio(ev);
    currentProgress.css({'width':ratio*100+'%'});
    audio.currentTime = audio.duration*ratio;
});

function getRatio(ev) {
    var totalWidth = totalProgress[0].offsetWidth;
    var totalX = totalProgress.offset().left;
    var mouseX = ev.clientX;
    var ratio = (mouseX - totalX) / totalWidth;
    return ratio;
}
// 格式化时间
function formatTime(time) {
    time = ~~time;
    var formatTime;
    if (time < 10){
        formatTime = '00:0' + time;
    } else if (time < 60){
        formatTime = '00:' + time;
    } else {
        var m = ~~(time/60);
        if(m < 10){
            m = '0' + m;
        }
        var s = time % 60;
        if (s < 10) {
            s = '0' + s;
        }
        formatTime = m + ':' + s;
    }
    return formatTime
}
// 计时
var timer = setInterval(function () {
    if(audio.ended){
        $('.play').css({'display':'inline-block'});
        $('.pause').css({'display':'none'});
        if (sb < 1){
            var rid = $('audio').attr('class');
            var id = $("[id="+ rid + "]").parent().next().children("td.name").attr('id');
            var hh = typeof id;
            if(hh !== 'undefined'){
                var song = $("[id="+ id + "]");
                var artist = song.next().contents()[0].nodeValue;
                var name = song.text();
                var time = song.attr('time');
                $('.song-name').text(name + ' -- ' + artist);
                totalTime.text(time);
                get_url(id);
            }
        sb++;
        }
    }else{
        currentTime.text(formatTime(audio.currentTime));
        var ratio = audio.currentTime / audio.duration;
        currentProgress.css({'width':ratio*100+'%'});
    }
},100);
// 获取搜索结果
// $('.yuan-right').click(function () {
//     $.ajax({
//         url: 'song:search_song',
//         type: 'get',
//         data: {
//             'word': $('.yuan-left').val(),
//         },
//         success: function (data) {
//             // var nick_name = $('#nick-name').text();
//             // if(nick_name===''){
//             //     alert('请先登陆');
//             // }else{
//             if(data.status === "SUCCESS"){
//                 $(".result").empty();
//                 if($('.result-list').hide()){
//                     $('.glyphicon-eye-open').click();
//                 }
//                 let total = data.info.length;
//                 for (var i=0;i<total;i++) {
//                     let id = data.info[i].rid;
//                     let time = data.info[i].songTimeMinutes;
//                     let name = data.info[i].name;
//                     let artist = data.info[i].artist;
//                     $('.result').append('<tr class="rid" style="cursor: pointer;"><th class="num"></th><td class="name"></td><td class="artist" style="max-width: 500px;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;"></td></tr>');
//                     $('.name').last().attr({'id': id, 'time': time}).html(name);
//                     $('.num').last().html(i + 1);
//                     $('.artist').last().html(artist + '<button onclick="clean(this)" type="button" class="close" aria-label="Close" style="color: #e8e6e5; opacity: 1; font-size: 15px; padding-right: 18px" ><span aria-hidden="true">&times;</span></button>');
//                     document.getElementById(id).addEventListener("click", function () {
//                         $('.song-name').text(name + ' -- ' + artist);
//                         totalTime.text(time);
//                         get_url(id);
//                     });
//                 }
//                 }else {
//                     $('.yuan-left').attr('placeholder','搜索内容不能为空！！');
//                 }
//
//         }
//     })
// })

// 清空单条搜索结果
function clean(doc){
    var tr = $(doc).parents('tr');
    var tr_long = tr.siblings().length;
    var tbody = document.getElementById('tbody');
    tr.remove();
    for (var i = 0; i<tr_long; i++) {
        tbody.rows[i].cells[0].innerText = i+1;
    }
}
// 上一首
function last_song(){
    var rid = $('audio').attr('class');
    var id = $("[id="+ rid + "]").parent().prev().children("td.name").attr('id');
    var hh = typeof id;
    if(hh === 'undefined'){
        $('.tip').text('没有上一首了！');
        window.setTimeout(hiddenMsg,800);
    }else{
        var song = $("[id=" + id + "]");
        var artist = song.next().contents()[0].nodeValue;
        var name = song.text();
        var time = song.attr('time');
        $('.song-name').text(name + ' -- ' + artist);
        totalTime.text(time);
        get_url(id);
    }
}
$('.glyphicon-step-backward').click(function () {
   last_song();
});
// 下一首
function next_song(){
    var rid = $('audio').attr('class');
    var id = $("[id="+ rid + "]").parent().next().children("td.name").attr('id');
    if(typeof id === 'undefined'){
        $('.tip').text('没有下一首了！');
        window.setTimeout(hiddenMsg,800);
    }else{
        var song = $("[id=" + id + "]");
        var artist = song.next().contents()[0].nodeValue;
        var name = song.text();
        var time = song.attr('time');
        $('.song-name').text(name + ' -- ' + artist);
        totalTime.text(time);
        get_url(id);
    }
}
$('.glyphicon-step-forward').click(function () {
    next_song();
});
function hiddenMsg() {
    $('.tip').text('');
}
// 点击图片播放/暂停背景声音
// $('video').click(function () {
//      if($(this).prop('muted')) {
//         $("video").prop('muted', false);
//     } else {
//         $("video").prop('muted', true);
//     }
// })
// 绑定键盘事件
$(document).keydown(function(event){
    // enter键
    if(event.keyCode===13){
        $('.yuan-right').click();
    }
    // 空格键
    if(event.keyCode===32){
        play_song();
    }
    // ←
    if(event.keyCode===37){
        $('.glyphicon-step-backward').click();
    }
    // →
    if(event.keyCode===39){
        $('.glyphicon-step-forward').click();
    }
})
