import mysql.connector
from flask import jsonify


try:

    con = mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="Ritik@1234",
                                                database="gym_database"
                                                )
    cursor = con.cursor(dictionary=True)
    print("connection sucesssfull")
    
except Exception as e:
    print("Error :" ,e)
    
    
    
def diet_plan_db(day):
    query= f"SELECT * FROM diet_plan WHERE day = '{day}'"
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify(data)

def weight_gain():
    diet = """Monday - Weight Gain Diet Plan
Breakfast:

3 scrambled eggs
2 slices of whole wheat toast with peanut butter
1 banana
1 cup of Greek yogurt
Mid-Morning Snack:

1 handful of almonds
1 apple
Lunch:

Grilled chicken breast
Brown rice
Steamed broccoli
Mixed salad with avocado dressing
Afternoon Snack:

Protein shake with whey protein, milk, banana, and oats
Dinner:

Baked salmon
Quinoa
Steamed asparagus
Sweet potato
Evening Snack:

Cottage cheese with pineapple slices
Tuesday - Weight Gain Diet Plan
Breakfast:

Protein oatmeal made with rolled oats, milk, protein powder, and berries
1 slice of whole wheat toast with avocado
Mid-Morning Snack:

Greek yogurt with honey and mixed nuts
Lunch:

Turkey and cheese sandwich on whole wheat bread
Carrot and cucumber sticks with hummus
Afternoon Snack:

Protein smoothie with banana, spinach, almond milk, and protein powder
Dinner:

Beef stir-fry with mixed vegetables
Brown rice
Evening Snack:

Whole wheat crackers with cheese slices
Wednesday to Sunday
Follow similar meal structures, incorporating a variety of lean proteins, healthy fats, complex carbohydrates, and vegetables into each meal. Ensure you're eating at regular intervals and consuming enough calories to support weight gain. Remember to stay hydrated by drinking plenty of water throughout the day.

Adjust portion sizes and meal frequency based on individual calorie and nutrient needs. It's also essential to combine this diet plan with a suitable exercise routine focused on strength training to promote muscle growth. Consulting with a nutritionist or dietitian can help tailor the plan to your specific goals and needs."""

    return  diet 


def weight_loss():
    diet = """Here's a sample weight loss diet plan:

Monday - Weight Loss Diet Plan
Breakfast:

Overnight oats made with rolled oats, almond milk, chia seeds, and mixed berries
1 boiled egg
Mid-Morning Snack:

Greek yogurt with sliced cucumber and carrot sticks
Lunch:

Grilled chicken salad with mixed greens, cherry tomatoes, cucumber, and balsamic vinaigrette dressing
Afternoon Snack:

Sliced apple with almond butter
Dinner:

Baked salmon with lemon and herbs
Steamed broccoli
Quinoa
Evening Snack:

Air-popped popcorn seasoned with herbs and spices
Tuesday - Weight Loss Diet Plan
Breakfast:

Spinach and feta omelette
Whole grain toast
Mid-Morning Snack:

Cottage cheese with pineapple chunks
Lunch:

Lentil soup
Mixed green salad with lemon vinaigrette
Afternoon Snack:

Celery sticks with hummus
Dinner:

Grilled tofu with stir-fried vegetables (bell peppers, onions, zucchini)
Brown rice
Evening Snack:

Herbal tea
Wednesday to Sunday
Follow a similar structure with a focus on lean protein sources, whole grains, fruits, vegetables, and healthy fats. Aim for balanced meals that include a variety of nutrients to keep you feeling satisfied and energized throughout the day.

In addition to following this diet plan, it's essential to stay hydrated by drinking plenty of water, limit sugary beverages and processed foods, and practice portion control. Regular physical activity, such as cardio and strength training exercises, can also support weight loss efforts and improve overall fitness levels.

Consulting with a healthcare professional or registered dietitian can help tailor the plan to your individual needs and goals, ensuring safe and effective weight loss.





"""
    return diet