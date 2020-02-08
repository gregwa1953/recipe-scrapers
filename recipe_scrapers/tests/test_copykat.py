# test_copykat.py
import os
import unittest

from recipe_scrapers.copykat import CopyKat


class TestCopyKat(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'copykat.testhtml'
        )) as file_opened:
            self.harvester_class = CopyKat(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'copyKat.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Make Tender Beef Tips in Gravy'
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual("10", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            'https://copykat.com/wp-content/uploads/2016/05/Beef-Tips-in-the-Instant-Pot-2-1.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 cup flour', '1 teaspoon salt', '1/4 teaspoon black pepper', '3 pounds lean chuck roast', '48 ounces beef stock', '1 tablespoon vegetable oil', '2 teaspoons gravy master', '1 cup onions chopped', '16 ounces noodles'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            ['In a small bowl add flour, salt, and pepper. Stir the salt and pepper into the flour. Cut and trim roast into small bite-sized pieces. Dredge beef pieces in seasoned flour shake off excess flour.\nSet the Instant Pot to saute, add oil. When the oil has heated drop in several pieces of the beef. Cook seasoned beef on all sides until lightly browned. Cook beef in small batches. When all of the beef is cooked add it back to the Instant Pot.\nAdd 1 cup of onion, two teaspoons of Gravy Master, and beef stock. Place lid on high and cook for 15 minutes on high pressure. Release pot after cooking with either a quick release or a natural release.',
                'Slow cooker directions', "Please use the same ingredients as listed below. For this recipe season your flour as mentioned in the recipe, then brown the meat in a large skillet in small batches with some vegetable oil. Add the beef broth you will simmer for 4 to 6 hours on low. If the liquid hasn't thickened up to your desire, you can thicken it up by mixing 1 tablespoon of butter and one tablespoon of flour that has been mixed together. Stir this in to the beef broth, and it will thicken up the liquid in the slow cooker."],
            self.harvester_class.instructions()
        )

    def test_ratings(self):
        self.assertEqual(
            "5 from 1 vote",
            self.harvester_class.ratings()
        )

    def test_description(self):
        self.assertEqual(
            'You can make amazingly tender beef tips in gravy.',
            self.harvester_class.description()
        )
