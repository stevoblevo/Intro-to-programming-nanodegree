// JavaScript Document
$(document).ready(function() {
$('.lesson-container').hide();
$('.note-text').hide();
$('.lesson').click(function() {
        $(this).next('.lesson-container').slideToggle('fast');
        return false;
    });
$('.note-title').click(function () {
        $(this).next('.note-text').slideToggle('fast');
        return false;
    });
//above found here: http://www.alohatechsupport.net/webdesignmaui/maui-web-site-design/show_hide_expand_collapse_javascript.html
    
$('.expand-all').click(function(){
        $('.lesson-container').slideDown('fast');
        $('.note-text').slideDown('fast')        
    });
$('.collapse-all').click(function(){
        $('.lesson-container').slideUp('fast');
        $('.note-text').slideUp('fast');
    });
});
