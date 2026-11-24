"""Extend the CTC posting tracker with a 40-day plan (Nov 25, 2026 - Jan 3, 2027).
python3 build_tracker.py <input.xlsx> <output.xlsx>"""
import sys, datetime as dt, copy
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

SRC, OUT = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(SRC)
D = dt.date
START, DAYS = D(2026, 11, 25), 40

# ---------------- Lists: add Daily cadence ----------------
L = wb['Lists']
if L['F6'].value is None:
    L['F6'] = 'Daily'; L['G6'] = 1
    L['G6'].font = copy.copy(L['G5'].font)

# ---------------- Topics: add the topics we now post about ----------------
T = wb['Topics']
existing = {T.cell(r, 2).value for r in range(2, T.max_row + 1)}
new_topics = [
    ('Math history stories', 'Lincoln studied Euclid', 'All grades', 'Monthly'),
    ('Math history stories', 'Perfect numbers', '5–6', 'Monthly'),
    ('Math history stories', 'Where the wheel came from', '5–6', 'Monthly'),
    ('Math history stories', 'Euler and Benjamin Franklin', '9–10', 'Monthly'),
    ('Math history stories', 'The people behind the math', 'All grades', 'Monthly'),
    ('Math history stories', 'Who decided a minute has 60 seconds', '5–6', 'Monthly'),
    ('Math history stories', 'Pythagoras and right triangles', '7–8', 'Monthly'),
    ('Math history stories', 'Where pi comes from', '7–8', 'Monthly'),
    ('Math history stories', 'Fibonacci and patterns in nature', '5–6', 'Monthly'),
    ('Math history stories', 'History of the calendar', 'All grades', 'Monthly'),
    ('Math history stories', 'Archimedes and Eureka', '9–10', 'Monthly'),
    ('Math tips and quick problems', 'Rounding and place value', '5–6', 'Every 2 weeks'),
    ('Math tips and quick problems', 'Perimeter in real life', '5–6', 'Every 2 weeks'),
    ('Math tips and quick problems', 'Adding large numbers', '5–6', 'Every 2 weeks'),
    ('Math tips and quick problems', 'Order of operations (PEMDAS)', '7–8', 'Every 2 weeks'),
    ('Math tips and quick problems', 'Problem of the Day', 'All grades', 'Daily'),
    ('Math tips and quick problems', '12 Days of Math holiday challenge', 'All grades', 'Daily'),
    ('Parent education', 'Math is one story', 'All grades', 'Monthly'),
    ('Parent education', 'Every topic has a prerequisite', 'All grades', 'Every 2 weeks'),
    ('Parent education', 'Winter break math slide', 'All grades', 'Weekly'),
    ('Parent education', 'New semester math plan', 'All grades', 'Monthly'),
    ('Founder and tutor authority', 'Thankful for teachers', 'All grades', 'Quarterly'),
    ('Founder and tutor authority', 'Behind the scenes: how a lesson is made', 'All grades', 'Monthly'),
    ('Offers and calls to action', 'Gift of Math prepaid year', 'All grades', 'Weekly'),
    ('Offers and calls to action', 'Free Saturday family webinar', 'All grades', 'Weekly'),
    ('Offers and calls to action', 'Live Class and Small Group', 'All grades', 'Weekly'),
    ('Offers and calls to action', 'Teacher training and PD for schools', 'All grades', 'Every 2 weeks'),
    ('Offers and calls to action', 'January enrollment', 'All grades', 'Weekly'),
]
row = 2
while T.cell(row, 2).value not in (None, ''):
    row += 1
tmpl = 2
for pillar, topic, grade, cad in new_topics:
    if topic in existing:
        continue
    for col in range(1, 10):
        src = T.cell(tmpl, col); dst = T.cell(row, col)
        dst._style = copy.copy(src._style)
        v = src.value
        if isinstance(v, str) and v.startswith('='):
            dst.value = v.replace(f'{tmpl}', f'{row}').replace(f'${2}', f'${row}') if False else v.replace(f'$B{tmpl}', f'$B{row}').replace(f'$D{tmpl}', f'$D{row}').replace(f'$F{tmpl}', f'$F{row}').replace(f'$E{tmpl}', f'$E{row}').replace(f'$G{tmpl}', f'$G{row}')
    T.cell(row, 1).value, T.cell(row, 2).value, T.cell(row, 3).value, T.cell(row, 4).value = pillar, topic, grade, cad
    row += 1
# widen the cadence lookup so "Daily" (Lists row 6) is found
for r in range(2, row):
    c = T.cell(r, 5)
    if isinstance(c.value, str):
        c.value = c.value.replace('Lists!$F$2:$G$5', 'Lists!$F$2:$G$10')
TOPIC_GRADE = {T.cell(r, 2).value: T.cell(r, 3).value for r in range(2, row)}
TOPIC_PILLAR = {T.cell(r, 2).value: T.cell(r, 1).value for r in range(2, row)}

# ---------------- Weekly Plan: add the 40-Day Plan level ----------------
W = wb['Weekly Plan']
W['I5'] = '40-Day Plan per week'
W['I5']._style = copy.copy(W['D5']._style)
W.column_dimensions['I'].width = 20
plan_targets = {  # (channel, format): per week
    ('Instagram', 'Reel'): 14, ('Instagram', 'Carousel'): 3, ('Instagram', 'Story'): 14, ('Instagram', 'Live'): 0,
    ('Facebook Page', 'Post'): 21, ('Facebook Group', 'Post'): 7, ('Facebook Group', 'Live'): 1,
    ('YouTube', 'Long-form video'): 1, ('YouTube', 'Short'): 7, ('YouTube', 'Live'): 0,
    ('LinkedIn', 'Post'): 5, ('X / Threads', 'Thread'): 0, ('Email', 'Newsletter'): 1, ('Podcast', 'Guest episode'): 0,
}
for r in range(6, 20):
    key = (W.cell(r, 1).value, W.cell(r, 2).value)
    W.cell(r, 9).value = plan_targets.get(key, 0)
    W.cell(r, 9)._style = copy.copy(W.cell(r, 4)._style)
    W.cell(r, 5).value = f'=IF($B$3="Maximum",D{r},IF($B$3="40-Day Plan",I{r},C{r}))'
W['I20'] = '=SUM(I6:I19)'; W['I20']._style = copy.copy(W['D20']._style)
W['B3'] = '40-Day Plan'
W.data_validations.dataValidation = []
dv = DataValidation(type='list', formula1='"Sustainable,Maximum,40-Day Plan"', allow_blank=False)
W.add_data_validation(dv); dv.add('B3')
W['A22'] = 'The 40-Day Plan level matches the channels connected today (both Facebook Pages, Instagram and YouTube through Posty; LinkedIn posted by hand). Facebook Page counts the Counting To Calculus Page; the same posts also go to the Learning Institute For Excellence Page. YouTube Shorts are capped at 7 a week while Posty is on its trial.'
W['A22'].alignment = Alignment(wrap_text=True, vertical='top'); W.merge_cells('A22:I23'); W.row_dimensions[22].height = 30

# ---------------- The 40-day calendar ----------------
morning = ['Fractions in 30 seconds', 'Rounding and place value', 'Negative numbers and integers', 'Solving one- and two-step equations',
           'Perimeter in real life', 'Ratios and percentages', 'Order of operations (PEMDAS)', 'Slope and linear graphs',
           'Adding large numbers', 'Quadratics and factoring', 'Common mistake of the week', 'Trigonometry basics',
           'Limits and derivatives made simple']
history = ['Euler and Benjamin Franklin', 'Gauss adds 1 to 100', 'History of zero and negative numbers', 'Where the wheel came from',
           'Al-Khwarizmi and the word algorithm', 'Pythagoras and right triangles', 'Who decided a minute has 60 seconds',
           'Hypatia of Alexandria', 'Where pi comes from', 'The people behind the math', 'Fibonacci and patterns in nature',
           'Lincoln studied Euclid', 'Euclid and the beginnings of geometry', 'History of the calendar', 'Archimedes and Eureka',
           'Perfect numbers', 'Newton, Leibniz and the birth of calculus']
hooks = {
    'Fractions in 30 seconds': 'If your 6th grader freezes at fractions, here is the missing step.',
    'Rounding and place value': 'Every math topic has a prerequisite. Rounding needs place value.',
    'Negative numbers and integers': 'Why is negative times negative positive? A 30-second answer.',
    'Solving one- and two-step equations': 'Algebra is just undoing. Watch.',
    'Perimeter in real life': 'How much paint does a soccer field need?',
    'Ratios and percentages': 'Is 20% off and then 20% off the same as 40% off?',
    'Order of operations (PEMDAS)': '48 - 17 + 9 - 6. Most adults get this wrong.',
    'Slope and linear graphs': 'Slope is just "how steep." Here is the picture.',
    'Adding large numbers': 'Add Houston + Dallas and you are doing real math.',
    'Quadratics and factoring': 'Factoring in 30 seconds: find two numbers that…',
    'Common mistake of the week': 'The mistake I see every week in middle school math.',
    'Trigonometry basics': 'SOH-CAH-TOA, explained with a ladder.',
    'Limits and derivatives made simple': 'Calculus in one sentence: how fast is it changing?',
    'Euler and Benjamin Franklin': 'Euler and Ben Franklin lived at the same time.',
    'Gauss adds 1 to 100': 'Can your child add 1 to 100 in 10 seconds? Gauss could.',
    'History of zero and negative numbers': 'Zero was invented. Who invented it?',
    'Where the wheel came from': 'Where did the wheel come from?',
    'Al-Khwarizmi and the word algorithm': 'The word "algorithm" is a person\'s name.',
    'Pythagoras and right triangles': 'Babylon knew a² + b² = c² 1,000 years before Pythagoras.',
    'Who decided a minute has 60 seconds': 'Who decided a minute has 60 seconds?',
    'Hypatia of Alexandria': 'Meet Hypatia, a mathematician of ancient Alexandria.',
    'Where pi comes from': 'Why 3.14? Where pi comes from.',
    'The people behind the math': 'Who were the people behind the math we teach?',
    'Fibonacci and patterns in nature': 'Count the spirals on a pinecone.',
    'Lincoln studied Euclid': 'Abraham Lincoln studied Euclid. Why don\'t our kids?',
    'Euclid and the beginnings of geometry': 'The most famous math book ever written is 2,300 years old.',
    'History of the calendar': 'Why does December mean "tenth month"?',
    'Archimedes and Eureka': 'Eureka! The bathtub that changed science.',
    'Perfect numbers': 'Why is 6 a "perfect" number?',
    'Newton, Leibniz and the birth of calculus': 'Two people invented calculus at the same time.',
}
ready = {  # topics that already have a finished short
    'Perimeter in real life': 'Ready: CTC_short_05 (soccer field)', 'Adding large numbers': 'Ready: CTC_short_04 (Houston + Dallas)',
    'Rounding and place value': 'Ready: CTC_short_03 (prerequisites)', 'Perfect numbers': 'Ready: CTC_short_02',
    'Lincoln studied Euclid': 'Ready: CTC_short_01', 'Where the wheel came from': 'Ready: CTC_short_07',
    'Euler and Benjamin Franklin': 'Ready: CTC_short_08', 'The people behind the math': 'Ready: CTC_short_09',
    'Who decided a minute has 60 seconds': 'Ready: CTC_short_10',
}
cut_from = {
    'Gauss adds 1 to 100': 'Cut from: Nov 1 Euler lesson (52 min)', 'Newton, Leibniz and the birth of calculus': 'Cut from: Nov 1 Euler lesson (52 min)',
    'History of the calendar': 'Cut from: Nov 1 time and calendar lesson (31 min)', 'Euclid and the beginnings of geometry': 'Cut from: Oct 31 shapes video',
    'Solving one- and two-step equations': 'Cut from: Algebra 1 & 2 session (43 min)', 'Quadratics and factoring': 'Cut from: Algebra 1 & 2 session (43 min)',
    'Slope and linear graphs': 'Cut from: Algebra 1 & 2 session (43 min)', 'Order of operations (PEMDAS)': 'Cut from: Jul 21 whiteboard (left to right)',
    'Negative numbers and integers': 'Cut from: Nov 23 "one story" series',
}
def asset(t):
    return ready.get(t) or cut_from.get(t) or 'Record (30–45 s)'

def week_theme(d):
    if d <= D(2026, 12, 1): return 'Thanksgiving week · Gift of Math (Black Friday to Giving Tuesday)'
    if d <= D(2026, 12, 6): return 'Close the gaps before winter break · Webinar Sat Dec 5'
    if d <= D(2026, 12, 13): return 'Mid-year report cards · Webinar Sat Dec 12 · ESA families'
    if d <= D(2026, 12, 25): return '12 Days of Math (Dec 14–25) · Winter break math slide'
    if d <= D(2026, 12, 31): return 'Winter break: keep learning · Year in review'
    return 'New year, new semester · January enrollment'

def evening(d, i):
    wd = d.weekday()
    special = {
        D(2026, 11, 26): ('Founder and tutor authority', 'Thankful for teachers', 'Happy Thanksgiving. I\'m thankful for the teachers who shaped me in Yola and Lagos.'),
        D(2026, 11, 27): ('Offers and calls to action', 'Gift of Math prepaid year', 'Black Friday: give the gift of math. Prepay the year, get one month free.'),
        D(2026, 11, 28): ('Offers and calls to action', 'Gift of Math prepaid year', 'Small Business Saturday: support a small school with a big mission.'),
        D(2026, 11, 30): ('Offers and calls to action', 'Gift of Math prepaid year', 'Cyber Monday: one month free when you prepay the year.'),
        D(2026, 12, 1): ('Offers and calls to action', 'Live Class and Small Group', 'Giving Tuesday: ask about multi-child and multi-subject scholarships.'),
        D(2026, 12, 5): ('Offers and calls to action', 'Free Saturday family webinar', 'TODAY: free family webinar on raising strong math students.'),
        D(2026, 12, 12): ('Offers and calls to action', 'Free Saturday family webinar', 'TODAY: free family webinar. How to use winter break well.'),
        D(2026, 12, 24): ('Founder and tutor authority', 'Behind the scenes: how a lesson is made', 'Merry Christmas Eve from the Counting to Calculus family.'),
        D(2026, 12, 25): ('Math tips and quick problems', '12 Days of Math holiday challenge', 'Day 12: the final holiday challenge. Merry Christmas!'),
        D(2026, 12, 31): ('Parent education', 'New semester math plan', 'One math goal for the new year. Here is how to pick it.'),
        D(2027, 1, 1): ('Offers and calls to action', 'January enrollment', 'Happy New Year! January classes start Monday. Book a free placement assessment.'),
    }
    if d in special: return special[d]
    if D(2026, 12, 2) <= d <= D(2026, 12, 4) or D(2026, 12, 9) <= d <= D(2026, 12, 11):
        return ('Offers and calls to action', 'Free Saturday family webinar', 'Free family webinar this Saturday: raising strong math students.')
    if d >= D(2027, 1, 2): return ('Offers and calls to action', 'January enrollment', 'New semester, new start. Seats are filling for January.')
    if d >= D(2026, 12, 14) and wd in (0, 3): return ('Parent education', 'Winter break math slide', 'Winter break erases math. 15 minutes a day stops it.')
    rot = [('Parent education', 'Signs your child is falling behind in pre-algebra', '3 signs your child is quietly falling behind in math.'),
           ('Offers and calls to action', 'Free Math Readiness Diagnostic', 'Find out exactly where your child is in math. Free.'),
           ('Parent education', 'Every topic has a prerequisite', 'Most math trouble is one missing building block.'),
           ('Founder and tutor authority', "Amos's story: from medical physics to math", 'From medical physics to math: why I teach.'),
           ('Parent education', 'Closing math gaps before high school', 'Close the gaps before high school. Here is how.'),
           ('Offers and calls to action', 'Live Class and Small Group', '4–6 students. One tutor who knows your child.'),
           ('Parent education', 'Why the AI era needs linear algebra', 'Why your child needs linear algebra to understand AI.'),
           ('Parent education', 'Using your ESA for live math, state by state', 'Homeschooling or using an ESA? Live math, counting to calculus.'),
           ('Parent education', 'Math is one story', 'Math isn\'t a pile of worksheets. It\'s one story.')]
    return rot[i % len(rot)]

def potd(d, i):
    if D(2026, 12, 14) <= d <= D(2026, 12, 25):
        return ('12 Days of Math holiday challenge', f'Day {(d - D(2026, 12, 14)).days + 1} of 12 Days of Math')
    return ('Problem of the Day', 'Problem of the Day (grade band rotates 5–6, 7–8, 9–10, 11–12)')

longform = {5: ['Euler: the master of us all (Nov 1 lesson, 52 min)', 'Telling time and the calendar (Nov 1 lesson, 31 min)',
                'Algebra 1 and 2 key concepts (43 min)', 'Math as one story: series opener (Nov 23, 9 min)',
                'Shapes and the wheel (Oct 31)', 'Perimeter and whole numbers (Jul 21 whiteboard set)']}

plan_rows, log_rows = [], []
for i in range(DAYS):
    d = START + dt.timedelta(i)
    wd = d.weekday()
    mt = morning[i % len(morning)]
    ht = history[i % len(history)]
    ep = evening(d, i)
    pt = potd(d, i)
    li = history[(i - 1) % len(history)] if wd < 5 else ''
    week_extra = []
    if wd == 5:
        week_extra.append('YouTube long-form: ' + longform[5][(i // 7) % len(longform[5])])
    if wd == 6:
        week_extra.append('Email newsletter (Sunday 5 PM MT)')
    if d in (D(2026, 12, 5), D(2026, 12, 12)):
        week_extra.append('Facebook Group Live: free family webinar, 12 PM ET')
    plan_rows.append(dict(
        date=d, day=d.strftime('%a'), theme=week_theme(d),
        am=f'{mt}\n"{hooks.get(mt, mt)}"\n[{asset(mt)}]',
        potd=f'{pt[1]}\n(Facebook Group + Instagram Story)',
        pm=f'{ht}\n"{hooks.get(ht, ht)}"\n[{asset(ht)}]',
        eve=f'{ep[1]}\n"{ep[2]}"',
        yt=f'{mt} (same video as 6:05 AM)',
        li=(f'{li}\n(LinkedIn 4:5 version, PD sign-off)' if li else '—'),
        extra='\n'.join(week_extra) or '—',
        todo=', '.join(sorted({a for a in (asset(mt), asset(ht)) if not a.startswith('Ready')})) or 'Nothing to record',
    ))
    if d == START:
        plan_rows[-1].update(
            am='ALREADY BOOKED in Posty:\n6:00 AM "Pick Your Time" ad video\n6:05 AM soccer field short (CTC_short_05)\n12:00 PM YouTube: Pick Your Time',
            pm='ALREADY BOOKED in Posty:\n10:05 AM "Math is one story" (CTC_short_06)\n12:00 PM "Small Group" ad video\n2:05 PM wheel (CTC_short_07)',
            eve='ALREADY BOOKED in Posty:\n6:05 PM Euler & Franklin (CTC_short_08)\n10:05 PM people behind the math (CTC_short_09)\nThu 2:05 AM 60 seconds (CTC_short_10)',
            yt='Already booked', todo='Nothing to record')
    # Post Log rows (planned)
    def add(channel, fmt, pillar, topic, hook, note=''):
        log_rows.append([d, channel, fmt, pillar, topic, TOPIC_GRADE.get(topic, 'All grades'), hook, None, 'Claude via Posty' if channel in ('Instagram', 'Facebook Page', 'YouTube') else 'Amos', 'Planned', None, None, None, note])
    add('Instagram', 'Reel', TOPIC_PILLAR.get(mt), mt, hooks.get(mt), '6:05 AM MT')
    add('Facebook Page', 'Post', TOPIC_PILLAR.get(mt), mt, hooks.get(mt), '6:05 AM MT · also Learning Institute Page')
    add('YouTube', 'Short', TOPIC_PILLAR.get(mt), mt, hooks.get(mt), '12:05 PM MT')
    add('Facebook Group', 'Post', 'Math tips and quick problems', pt[0], pt[1], '10:05 AM MT')
    add('Instagram', 'Story', 'Math tips and quick problems', pt[0], pt[1], '10:05 AM MT')
    add('Instagram', 'Reel', TOPIC_PILLAR.get(ht), ht, hooks.get(ht), '2:05 PM MT')
    add('Facebook Page', 'Post', TOPIC_PILLAR.get(ht), ht, hooks.get(ht), '2:05 PM MT · also Learning Institute Page')
    add('Facebook Page', 'Post', ep[0], ep[1], ep[2], '6:05 PM MT · also Learning Institute Page')
    add('Instagram', 'Story', ep[0], ep[1], ep[2], '6:05 PM MT')
    if wd in (0, 2, 4):
        add('Instagram', 'Carousel', ep[0], ep[1], ep[2], '6:05 PM MT')
    if li:
        add('LinkedIn', 'Post', TOPIC_PILLAR.get(li), li, hooks.get(li), '7:05 AM MT (9:05 AM ET) · post by hand unless LinkedIn is in Posty')
    if wd == 5:
        add('YouTube', 'Long-form video', 'Math history stories', 'The people behind the math', longform[5][(i // 7) % len(longform[5])], 'Saturday 9 AM MT')
    if wd == 6:
        add('Email', 'Newsletter', 'Parent education', 'Every topic has a prerequisite', 'Weekly family newsletter', 'Sunday 5 PM MT')
    if d in (D(2026, 12, 5), D(2026, 12, 12)):
        add('Facebook Group', 'Live', 'Offers and calls to action', 'Free Saturday family webinar', 'Free family webinar', '10 AM MT / 12 PM ET')

# ---------------- Post Log: what is already published or scheduled ----------------
P = wb['Post Log']
done = [  # (date, channel, format, pillar, topic, hook, link, status, note)
    (D(2026,11,24),'Facebook Page','Post','Offers and calls to action','Live Class and Small Group','Meet Amos: top of the class? That\'s where we start.','https://www.facebook.com/1868132251009749','Posted','Ad video · also Learning Institute Page'),
    (D(2026,11,24),'Instagram','Reel','Offers and calls to action','Live Class and Small Group','Meet Amos: top of the class? That\'s where we start.','https://www.instagram.com/reel/DgIzjN2EVBQ/','Posted','Ad video'),
    (D(2026,11,24),'YouTube','Short','Offers and calls to action','Live Class and Small Group','Meet Amos: top of the class? That\'s where we start.','https://www.youtube.com/watch?v=uRQLGwbIjcE','Posted','Ad video'),
    (D(2026,11,24),'Facebook Page','Post','Math history stories','Lincoln studied Euclid','Abraham Lincoln studied Euclid. Why don\'t our kids?','https://www.facebook.com/3075448682790024','Posted','CTC_short_01 · also Learning Institute Page'),
    (D(2026,11,24),'Instagram','Reel','Math history stories','Lincoln studied Euclid','Abraham Lincoln studied Euclid. Why don\'t our kids?','https://www.instagram.com/reel/DgI4gwrip1T/','Posted','CTC_short_01'),
    (D(2026,11,24),'Facebook Page','Post','Math history stories','Perfect numbers','Why is 6 a "perfect" number?',None,'Scheduled','6:05 PM MT · CTC_short_02'),
    (D(2026,11,24),'Instagram','Reel','Math history stories','Perfect numbers','Why is 6 a "perfect" number?',None,'Scheduled','6:05 PM MT'),
    (D(2026,11,24),'Facebook Page','Post','Offers and calls to action','Free Math Readiness Diagnostic','Find the gaps. Close the gaps. Move forward.',None,'Scheduled','7:00 PM MT · Close the Gaps ad video'),
    (D(2026,11,24),'Instagram','Reel','Offers and calls to action','Free Math Readiness Diagnostic','Find the gaps. Close the gaps. Move forward.',None,'Scheduled','7:00 PM MT'),
    (D(2026,11,24),'Facebook Page','Post','Parent education','Every topic has a prerequisite','Every math topic has a prerequisite.',None,'Scheduled','10:05 PM MT · CTC_short_03'),
    (D(2026,11,24),'Instagram','Reel','Parent education','Every topic has a prerequisite','Every math topic has a prerequisite.',None,'Scheduled','10:05 PM MT'),
    (D(2026,11,25),'Facebook Page','Post','Math tips and quick problems','Adding large numbers','Add Houston + Dallas and you\'re doing real math.',None,'Scheduled','2:05 AM MT · CTC_short_04'),
    (D(2026,11,25),'Instagram','Reel','Math tips and quick problems','Adding large numbers','Add Houston + Dallas and you\'re doing real math.',None,'Scheduled','2:05 AM MT'),
    (D(2026,11,25),'Facebook Page','Post','Offers and calls to action','Live Class and Small Group','Pick a time. Your child learns live.',None,'Scheduled','6:00 AM MT · Pick Your Time ad video'),
    (D(2026,11,25),'Instagram','Reel','Offers and calls to action','Live Class and Small Group','Pick a time. Your child learns live.',None,'Scheduled','6:00 AM MT'),
    (D(2026,11,25),'Facebook Page','Post','Math tips and quick problems','Perimeter in real life','How much paint does a soccer field need?',None,'Scheduled','6:05 AM MT · CTC_short_05'),
    (D(2026,11,25),'Instagram','Reel','Math tips and quick problems','Perimeter in real life','How much paint does a soccer field need?',None,'Scheduled','6:05 AM MT'),
    (D(2026,11,25),'Facebook Page','Post','Parent education','Math is one story','Math isn\'t a pile of worksheets. It\'s one story.',None,'Scheduled','10:05 AM MT · CTC_short_06'),
    (D(2026,11,25),'Instagram','Reel','Parent education','Math is one story','Math isn\'t a pile of worksheets. It\'s one story.',None,'Scheduled','10:05 AM MT'),
    (D(2026,11,25),'Facebook Page','Post','Offers and calls to action','Live Class and Small Group','4–6 students. One tutor who knows your child.',None,'Scheduled','12:00 PM MT · Small Group ad video'),
    (D(2026,11,25),'Instagram','Reel','Offers and calls to action','Live Class and Small Group','4–6 students. One tutor who knows your child.',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,25),'YouTube','Short','Offers and calls to action','Live Class and Small Group','Pick a time. Your child learns live.',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,25),'Facebook Page','Post','Math history stories','Where the wheel came from','Where did the wheel come from?',None,'Scheduled','2:05 PM MT · CTC_short_07'),
    (D(2026,11,25),'Instagram','Reel','Math history stories','Where the wheel came from','Where did the wheel come from?',None,'Scheduled','2:05 PM MT'),
    (D(2026,11,25),'Facebook Page','Post','Math history stories','Euler and Benjamin Franklin','Euler and Ben Franklin lived at the same time.',None,'Scheduled','6:05 PM MT · CTC_short_08'),
    (D(2026,11,25),'Instagram','Reel','Math history stories','Euler and Benjamin Franklin','Euler and Ben Franklin lived at the same time.',None,'Scheduled','6:05 PM MT'),
    (D(2026,11,25),'Facebook Page','Post','Math history stories','The people behind the math','Who were the people behind the math we teach?',None,'Scheduled','10:05 PM MT · CTC_short_09'),
    (D(2026,11,25),'Instagram','Reel','Math history stories','The people behind the math','Who were the people behind the math we teach?',None,'Scheduled','10:05 PM MT'),
    (D(2026,11,26),'Facebook Page','Post','Math history stories','Who decided a minute has 60 seconds','Who decided a minute has 60 seconds?',None,'Scheduled','2:05 AM MT · CTC_short_10'),
    (D(2026,11,26),'Instagram','Reel','Math history stories','Who decided a minute has 60 seconds','Who decided a minute has 60 seconds?',None,'Scheduled','2:05 AM MT'),
    (D(2026,11,26),'YouTube','Short','Offers and calls to action','Free Math Readiness Diagnostic','Find the gaps. Close the gaps. Move forward.',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,27),'YouTube','Short','Offers and calls to action','Live Class and Small Group','4–6 students. One tutor who knows your child.',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,28),'YouTube','Short','Math history stories','Lincoln studied Euclid','Abraham Lincoln studied Euclid. Why don\'t our kids?',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,29),'YouTube','Short','Math history stories','Perfect numbers','Why is 6 a "perfect" number?',None,'Scheduled','12:00 PM MT'),
    (D(2026,11,30),'YouTube','Short','Parent education','Every topic has a prerequisite','Every math topic has a prerequisite.',None,'Scheduled','12:00 PM MT'),
    (D(2026,12,1),'YouTube','Short','Math tips and quick problems','Adding large numbers','Add Houston + Dallas and you\'re doing real math.',None,'Scheduled','12:00 PM MT'),
    (D(2026,12,2),'YouTube','Short','Math tips and quick problems','Perimeter in real life','How much paint does a soccer field need?',None,'Scheduled','12:00 PM MT'),
]
# planned rows that collide with what is already booked: Nov 25 reels/FB (slots taken), YouTube Nov 25 - Dec 2 (one a day, already booked)
booked_days_reels = {D(2026, 11, 25)}
yt_booked = {D(2026, 11, 25) + dt.timedelta(k) for k in range(8)}
log_rows = [r for r in log_rows if not ((r[0] in booked_days_reels and r[1] in ('Instagram', 'Facebook Page') and r[2] in ('Reel', 'Post'))
                                        or (r[0] in yt_booked and r[1] == 'YouTube' and r[2] == 'Short'))]
all_rows = [[d, c, f, p, t, TOPIC_GRADE.get(t, 'All grades'), h, link, 'Claude via Posty', st, None, None, None, n] for d, c, f, p, t, h, link, st, n in done] + log_rows
all_rows.sort(key=lambda r: (r[0], r[13] or ''))
style_src = [P.cell(2, c)._style for c in range(1, 16)]
for r in range(2, 1001):
    for c in [1] + list(range(3, 16)):
        P.cell(r, c).value = None
for k, rr in enumerate(all_rows):
    r = 2 + k
    vals = [rr[0], None] + rr[1:]
    for c in range(1, 16):
        if c == 2:
            continue
        cell = P.cell(r, c); cell._style = copy.copy(style_src[c - 1]); cell.value = vals[c - 1]
print('post log rows:', len(all_rows))

# ---------------- 40-Day Plan sheet ----------------
if '40-Day Plan' in wb.sheetnames:
    del wb['40-Day Plan']
S = wb.create_sheet('40-Day Plan', 1)
head = ['Date', 'Day', 'Theme', '6:05 AM MT · Reel (both FB Pages + IG; YouTube Short 12:05 PM)', '10:05 AM MT · Problem of the Day',
        '2:05 PM MT · Reel (both FB Pages + IG)', '6:05 PM MT · Evening post (both FB Pages + IG Story; IG carousel Mon/Wed/Fri)',
        'LinkedIn · 7:05 AM MT (weekdays)', 'Weekly extras', 'To record or cut']
navy = PatternFill('solid', fgColor='0B2470'); gold = PatternFill('solid', fgColor='FFF3C4'); thin = Side(style='thin', color='C9D3EE')
S['A1'] = 'Counting to Calculus · 40-day posting plan (Nov 25, 2026 – Jan 3, 2027)'
S['A1'].font = Font(bold=True, size=14, color='0B2470')
S['A2'] = ('Four posts a day every 4 hours (Mountain time), plus a daily YouTube Short, weekday LinkedIn, a Saturday long-form video and a Sunday email. '
           'Captions open with the hook and put prices at the bottom. LinkedIn versions close with teacher training and PD (support@countingtocalculus.org), no prices. '
           'Nov 25–26 slots and YouTube through Dec 2 are already booked in Posty (see the Post Log).')
S['A2'].alignment = Alignment(wrap_text=True, vertical='top'); S.merge_cells('A2:J2'); S.row_dimensions[2].height = 48
for c, h in enumerate(head, 1):
    cell = S.cell(4, c, h); cell.font = Font(bold=True, color='FFFFFF'); cell.fill = navy
    cell.alignment = Alignment(wrap_text=True, vertical='center')
S.row_dimensions[4].height = 46
widths = [11, 6, 30, 36, 28, 36, 36, 30, 30, 28]
for c, w in enumerate(widths, 1):
    S.column_dimensions[get_column_letter(c)].width = w
for k, pr in enumerate(plan_rows):
    r = 5 + k
    vals = [pr['date'], pr['day'], pr['theme'], pr['am'], pr['potd'], pr['pm'], pr['eve'], pr['li'], pr['extra'], pr['todo']]
    for c, v in enumerate(vals, 1):
        cell = S.cell(r, c, v)
        cell.alignment = Alignment(wrap_text=True, vertical='top')
        cell.border = Border(bottom=thin)
        if pr['date'].weekday() >= 5:
            cell.fill = gold
    S.cell(r, 1).number_format = 'mmm d'
    S.row_dimensions[r].height = 64
S.freeze_panes = 'D5'

# ---------------- Read me ----------------
R = wb['Read me']
r = 3
while R.cell(r, 1).value:
    r += 1
R.insert_rows(5)
R['A5'] = '40-Day Plan'
R['B5'] = ('Day-by-day calendar from Nov 25, 2026 to Jan 3, 2027: what goes out in each 4-hour slot, the hook, and whether the video is ready, '
           'can be cut from existing footage, or needs recording. Every planned post is also a row in the Post Log marked Planned; '
           'the daily check-in marks rows Scheduled or Posted and fills in views and engagements.')
for c in ('A5', 'B5'):
    R[c]._style = copy.copy(R['A6' if c == 'A5' else 'B6']._style)

# ---- fix two formula problems that were in the original file ----
# 1) MAXIFS must be stored with the _xlfn. prefix or Excel/LibreOffice show #NAME?
for r in range(2, T.max_row + 1):
    c = T.cell(r, 6)
    if isinstance(c.value, str) and 'MAXIFS(' in c.value and '_xlfn.MAXIFS(' not in c.value:
        c.value = c.value.replace('MAXIFS(', '_xlfn.MAXIFS(')
# 2) 'Week starting' was one array formula with a calculation inside an array constant (#N/A); use a plain formula per row
P['B1'] = 'Week starting'
for r in range(2, 1001):
    P.cell(r, 2).value = f'=IF(A{r}="","",A{r}-WEEKDAY(A{r},3))'
    P.cell(r, 2).number_format = 'mmm d, yyyy'
wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print('saved', OUT)
