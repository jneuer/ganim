import ganim as ga
from ganim.line_elements import DoLineSegment

ga.reset_default_style()

s1 = ga.Scene()
s1.add_part(
    [
        DoLineSegment((0, 0), (4, 3), color='green', stay=False)
    ],
    duration=1
)

s1.add_part(
    [
        DoLineSegment((4, 0), (4, 3), color='blue', effect='grow'),
        DoLineSegment((0, 0), (4, 0), color='red', effect='grow')
    ],
    duration=1
)

print(f'Rendering scene s1:\n{s1}...')
s1.render()
print('Saving...')
s1.save('08-stay.mp4')
