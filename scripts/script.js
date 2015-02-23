// JavaScript Document
$(document).ready(function() {
$('div.lesson-container').hide();
$('div.note-text').hide();
$('div.lesson').click(function() {
        $(this).next('div.lesson-container').slideToggle('fast');
        return false;
    });
$('div.note-title').click(function () {
        $(this).next('div.note-text').slideToggle('fast');
        return false;
    });
//above found here: http://www.alohatechsupport.net/webdesignmaui/maui-web-site-design/show_hide_expand_collapse_javascript.html
    
$('div.expand-all').click(function(){
        $('.lesson-container').slideDown('fast');
        $('.note-text').slideDown('fast')        
    });
$('div.collapse-all').click(function(){
        $('.lesson-container').slideUp('fast');
        $('.note-text').slideUp('fast');
    });
});
