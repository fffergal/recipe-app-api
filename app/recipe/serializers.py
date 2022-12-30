from rest_framework import serializers

from core.models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name"]


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ["id", "title", "time_minutes", "price", "link", "ingredients"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients", None)
        recipe = super().create(validated_data)
        if ingredients:
            for ingredient in ingredients:
                Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients", None)
        recipe = super().update(instance, validated_data)
        if ingredients:
            Ingredient.objects.filter(recipe=recipe).delete()
            for ingredient in ingredients:
                Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe


class RecipeDetailSerializer(RecipeSerializer):
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description"]
