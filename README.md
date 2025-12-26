# Interview Part 2: GitHub Edition

This project is a collaborative collection of simple HTML recipes. You can use AI tools to help you!

---

## How to Clone and Setup

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

### 0. Approve a random pr with a nice comment at the below list
https://github.com/SCE-Development/git-workshop/pulls

### 1. Add Your Own Recipe
- Create a new `.html` file with your recipe.
- Link to it from `index.html`.
- In your pull request description, **include a screenshot** of your recipe page.

### 2. Delete an Existing Recipe
- On a separate branch, open a PR that **deletes an existing recipe**. Make sure that your PR deletes both the file AND the recipe entry in `index.html`. In your PR description, tell us why your new recipe that you created in Step 1 is better than the recipe you deleted here.

### 3. Add a "Food Critic" or "Recipe Lore" Section
- On a third branch that branches **from the same branch as your recipe PR**, add a `<div>` below your recipe labeled **"Food Critic Review"** ,  **"Recipe Lore"**, or something similar
- Add a description under this `<div>` that **corresponds to your section title**
    - We want these to be personalized, so be creative!
    - Make up whatever wacky addition you want!
- This PR should **depend on the recipe PR** and point to your original recipe branch
- In this PR description, add a note like `merge #NUMBER first!`

## A completed 3 pull requests should look like:
```
main
 │
 ├───▶ YOUR_NAME/DATE_add-my-recipe       (PR #1: Your new recipe)
 │    │
 │    └──▶ YOUR_NAME/DATE_add-food-critic-or-recipe-lore (PR #3: Review section)
 │
 └───▶ YOUR_NAME/DATE_remove-box-of-cereal     (PR #2: Removes existing recipe)
```

for an example of the 3 PRs, see:
- [#24](https://github.com/SCE-Development/git-workshop/pull/24) as step 1,
adding the recipe
- [#330](https://github.com/SCE-Development/git-workshop/pull/330) as step 2,
deleting an existing recipe
- [#26](https://github.com/SCE-Development/git-workshop/pull/26) as step 3,
branching off of step 1, and the pr pointing to step 1 instead of main
