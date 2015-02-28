# This is the "generate_note_HTML" function
def generate_note_HTML(note_title, note_text, lesson_number, note_number):
    html_text_1 = '''
  <article class="note" id="lesson-'''+str(lesson_number)+'-'+str(note_number)+'''">
     <header class="note-title">
       ''' + note_title
    html_text_2 = '''
     </header>
     <div class="note-text">
       <p>''' + note_text
    html_text_3 = '''
       </p>
     </div>
  </article>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def generate_lesson_HTML(lesson_title, lesson_text, lesson_number):
    html_text_1 = '''
<header class="lesson" id="lesson-'''+str(lesson_number)+'''">
   <h3> '''+lesson_title+''' <h3>
<header>
<section class="lesson-container">'''
    html_text_2 = make_HTML_for_many_notes(lesson_text, lesson_number)
    html_text_3 = '''
</section>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_lesson_HTML(lesson, lesson_number):
    lesson_title = lesson[0]
    lesson_text = lesson[1]
    return generate_lesson_HTML(lesson_title, lesson_text, lesson_number)
    
def make_note_HTML(note, lesson_number, note_number):
    note_title = note[0]
    note_text = note[1]
    return generate_note_HTML(note_title, note_text, lesson_number, note_number)

# This is an example of what a list of concepts might look like.
LIST_OF_NOTES = [ ['Python', 'Python is a Programming Language'],
                  ['For Loop', 'For Loops allow you to iterate over lists'],
                  ['Lists', 'Lists are sequences of data'] ]
LIST_OF_LESSONS = [ ['lesson 1', LIST_OF_NOTES], ['lesson 2', LIST_OF_NOTES] ]

# Generate HTML for multiple notes
def make_HTML_for_many_notes(list_of_notes, lesson_number):
    HTML_code=''
    i=0
    for e in list_of_notes:
        i=i+1
        HTML_code=HTML_code+make_note_HTML(e, lesson_number, i)
    return HTML_code

# Generate HTML for multiple lessons
def make_HTML_for_many_lessons(list_of_lessons, lesson_number):
    HTML_code=''
    i=lesson_number
    for lesson in list_of_lessons:
        HTML_code=HTML_code+make_lesson_HTML(lesson, i)
        i=i+1
    return HTML_code
        

# testing
print make_HTML_for_many_lessons(LIST_OF_LESSONS,3)