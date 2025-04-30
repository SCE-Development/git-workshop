# Interview Part 2: GitHub Edition

This project is a collaborative collection of simple HTML recipes. You can use AI tools to help you!

---

## 🚀 How to Clone and Setup

1. Clone the repo:
```bash
git clone https://github.com/SCE-Development/git-workshop.git
cd git-workshop
```
2. Once you're in the project directory, run the below command. It will
output a file path, which you can copy and paste into your browser URL input
to open the project.
```
echo "$(pwd)/index.html"
```

If on windows:
```
echo %cd%\index.html
```

## Contributing
Make **3 pull requests** as described below. Branch names should follow a convention of:

`NAME/DATE_short_description`, i.e. `andy/20270601_add_pancake_recipe`

### 1. Add Your Own Recipe
- Create a new `.html` file with your recipe.
- Link to it from `index.html`.
- In your pull request description, **include a screenshot** of your recipe page.

### 2. Modify an Existing Recipe
- On a separate branch, open a PR that **changes one ingredient or step** in an existing recipe.

### 3. Add a "Food Critic" Section
- On a third branch that branches **from the same branch as your recipe PR**, add a `<div>` below your recipe labeled **"Food Critic Review"** or similar.
- This PR should **depend on the recipe PR** and point to your original recipe branch
- In this PR description, add a note like `merge #NUMBER first!`

## A completed 3 pull requests should look like:
```
main
 │
 ├───▶ YOUR_NAME/DATE_add-my-recipe       (PR #1: Your new recipe)
 │    │
 │    └──▶ YOUR_NAME/DATE_add-food-critic (PR #3: Review section)
 │
 └───▶ YOUR_NAME/DATE_update-existing     (PR #2: Edits existing recipe)
```
