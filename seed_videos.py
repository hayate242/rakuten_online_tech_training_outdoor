from models.database import db_session

"""[videos seeder]
"""
from models.models import Videos
# exercise
db_session.add(
    Videos(
        '5MIN BOOTY & AB WORKOUT // Yoga Ball | Pamela RF',
        '2020/9/15',
        'The video is in full length which means you can just follow whatever I’m doing! 30 seconds each exercise – NO REST IN BETWEEN.',
        '',
        'https://youtu.be/iY4hQd24_d0', 'exercise'
    )
)
db_session.add(
    Videos(
        '5 MIN HOME WORKOUT YOU CAN DO EVERY MORNING',
        '2020/9/14',
        "Today's workout is the great routine you can follow every morning without making noise at home. To increase our energy, let's move and do workout together :)",
        '',
        'https://youtu.be/fLLScgWQcHc', 'exercise'
    )
)
db_session.add(
    Videos(
        '5-Minute Warm Up for At-Home Workouts',
        '2020/9/13',
        "This 5-minute warm up is made with the at-home workouts. We'll start with two minutes of cardio bodyweight exercises and then move onto active stretches for a functional range of motion.",
        '',
        'https://youtu.be/Ks-lKvKQ8f4', 'exercise'
    )
)
db_session.add(
    Videos(
        '5 MIN UPPER BODY WORKOUT (NO EQUIPMENT NEEDED)',
        '2020/9/12',
        "The video is in full length which means you can just follow whatever I’m doing! 30 seconds each exercise – NO REST IN BETWEEN.",
        '',
        'https://youtu.be/1fjeQKI-5wg', 'exercise'
    )
)

# recipe
db_session.add(
    Videos(
        "Salads: Cucumber Tomato Avocado Salad Recipe - Natasha's Kitchen",
        '2020/9/15',
        'This Cucumber Tomato Avocado Salad recipe is a keeper! Easy, Excellent Salad with a light, flavorful lemon dressing and freshness of cilantro.',
        '',
        'https://youtu.be/SpI3QF_Iauc', 'recipe'
    )
)
db_session.add(
    Videos(
        'How To Make Creamy Shrimp Alfredo Pasta - 30 Minute Meal',
        '2020/9/14',
        "A must try creamy shrimp Alfredo pasta! It is surprisingly easy to make and is ready in under 30 minutes. This Shrimp Fettuccine is major comfort food.",
        '',
        'https://youtu.be/5vy9HeL8mOc', 'recipe'
    )
)
db_session.add(
    Videos(
        'How To Make Italian PASTA SALAD with Homemade ITALIAN DRESSIN',
        '2020/9/13',
        "This Italian pasta salad recipe is loaded with fresh and colorful vegetables, cheese, salami, and homemade Italian dressing.  Toss with your favorite pasta to create an unforgettable dish.",
        '',
        'https://youtu.be/21rgi2Imq14', 'recipe'
    )
)
db_session.add(
    Videos(
        'Easy Pan Seared Salmon Recipe with Lemon Butter',
        '2020/9/12',
        "A simple, elegant Pan Seared Salmon recipe in a lemon browned butter sauce. Master this easy (10 minute) method for how to cook salmon in a pan. You won’t believe the easy ingredients!",
        '',
        'https://youtu.be/-x2E7T3-r7k', 'recipe'
    )
)
db_session.commit()
