# article-summarizer
Article summarizer with a focus on recipe articles. Online recipes specifically are bogged by ads, auto-playing videos, and lengthy preambles. This should grab only the essential information (ingredients and directions), ideally.

# Example: 

###### Summary
Ingredients
1/2 cup sugar
1/2 cup packed brown sugar
3 tablespoons all-purpose flour
1 teaspoon ground cinnamon
1/4 teaspoon ground ginger
1/4 teaspoon ground nutmeg
6 to 7 cups thinly sliced peeled tart apples
1 tablespoon lemon juice
Pastry for double-crust pie
1 tablespoon butter
1 large egg white
Additional sugar
Directions
In a small bowl, combine the sugars, flour and spices; set aside. In a large bowl, toss apples with lemon juice. Add sugar mixture; toss to coat.
Line a 9-in. pie plate with bottom crust; trim even with edge. Fill with apple mixture; dot with butter. Roll remaining crust to fit top of pie; place over filling. Trim, seal and flute edges. Cut slits in crust.
Beat egg white until foamy; brush over crust. Sprinkle with sugar. Cover edges loosely with foil.
Bake at 375° for 25 minutes. Remove foil and bake until crust is golden brown and filling is bubbly, 20-25 minutes longer. Cool on a wire rack.

###### Original Article
Ingredients
1/2 cup sugar
1/2 cup packed brown sugar
3 tablespoons all-purpose flour
1 teaspoon ground cinnamon
1/4 teaspoon ground ginger
1/4 teaspoon ground nutmeg
6 to 7 cups thinly sliced peeled tart apples
1 tablespoon lemon juice
Pastry for double-crust pie
1 tablespoon butter
1 large egg white
Additional sugar
Directions
In a small bowl, combine the sugars, flour and spices; set aside. In a large bowl, toss apples with lemon juice. Add sugar mixture; toss to coat.
Line a 9-in. pie plate with bottom crust; trim even with edge. Fill with apple mixture; dot with butter. Roll remaining crust to fit top of pie; place over filling. Trim, seal and flute edges. Cut slits in crust.
Beat egg white until foamy; brush over crust. Sprinkle with sugar. Cover edges loosely with foil.
Bake at 375° for 25 minutes. Remove foil and bake until crust is golden brown and filling is bubbly, 20-25 minutes longer. Cool on a wire rack.
Love Baking? Join Bakeable, Taste of Home's community dedicated to the joy of baking. Subscribe to the Bakeable newsletter and join the Facebook group where you’ll find recipes, tips and monthly challenges.
Apple Pie Tips
What are the best apples to use in pies?
In the Taste of Home Test Kitchen, we prefer using Granny Smith for pies because of its tart flavor and ability to hold its shape. If you want something with a little more sweetness, we recommend using Braeburn, Golden Delicious or Jonagold. Learn more about the best apples for apple pie to determine which is the best one for you!
How many apples are in 6 cups?
Typically, 1 medium apple yields 1-1/3 cups sliced. For 6 cups of sliced apples, you will need about 5 medium apples. Plus, you'll have a little left over for a snack or to use in any of these apple recipes!
How do you keep the bottom of a pie from getting soggy?
To avoid a pie bottom from getting soggy, allow the bottom crust to heat more rapidly than the rest of the pie. To do this, place a baking sheet in the oven while preheating and then bake your pie on the pan.
Is it better to bake a pie in glass or metal?
Both metal and glass pie plates work well for baking double-crust pies. But for single-crust pies that are pre-baked, a metal plate is preferred because it heats quicker and ensures a crisp crust. Follow our other pie baking tips in our ultimate pie baking guide!
How do I keep my pie filling from being watery?
To prevent your pie from getting watery, make sure to have your pie crust ready before mixing the filling. The longer the filling sits before baking, the more moisture it will release. Follow these best-kept pie crust secrets so your crust can hold your pie filling nice and strong!
Nutrition Facts
1 piece: 414 calories, 16g fat (7g saturated fat), 14mg cholesterol, 227mg sodium, 67g carbohydrate (38g sugars, 2g fiber), 3g protein.

# Algorithm
###### General summarizing
* 1 ) Word association (e.g. 'City', 'Cities')
* 2 ) Calculate occurences of each word in the artic
* 3 ) Assign each word a ranking based on the occurences
* 4 ) Detect periods that do not represent end of sentences (e.g. 'Mr.' is not a full stop)
* 5 ) Split article into individual sentences
* 6 ) Rank sentences based on the sum of the ranking of the words in them
* 7 ) Return X of the most highly ranked sentences in chronological order
