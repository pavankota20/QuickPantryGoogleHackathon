# -*- coding: utf-8 -*-

import google.generativeai as genai

class RecipeAssistant:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def get_ingredient_list(self, user_input):
        content = '''Craft a list of essential ingredients necessary for preparing a chosen recipe. Please format your response by listing each component distinctly. The list should encompass all foundational items necessary for the recipe, avoiding any superfluous commentary or symbols. Your enumeration should follow this format:

                        Ingredient 1;
                        Ingredient 2;
                        Ingredient 3;
                        
                        Ensure the list is comprehensive without any bullet points, covering the variety of ingredients that blend together to create the full experience of the chosen dish.'''
        
        content += user_input
        response = self.model.generate_content(content).text
        response = response.split(';')
        trimmed = [string.strip() for string in response]
        return trimmed