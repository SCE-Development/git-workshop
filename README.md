# git-workshop
#### Welcome to the Git Workshop hosted by SCE

Today we are going to learn the following: 
- What is Git/GitHub
- Basic Version Control
- Pulling and Pushing Branches
- Switching/Creating Branches 

---
### First Steps:
1. Install Git
  - If you dont have Git installed, you will need to install it onto your operating system

| Operating System | Relevant Links |
| --- | --- |
| Windows | [Link Here](https://git-scm.com/download/win) |
| Mac | [Link Here](https://git-scm.com/download/mac) |
| Linux | [Link Here](https://git-scm.com/download/linux) |

<details>
<summary> Additional Notes for Mac</summary>
  - There are several ways to install git onto your system. of the options, we reccomend homebrew which you can install with the following command:

  ```
 $(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)
  ```

</details>

---
### Cloning the repo:
2. Next lets try cloning the repo. 
- For this we will be using <code style="color:#A9FFF7">git clone</code>.
- Make sure you are in the folder you want to put the repo into

```
git clone https://github.com/SCE-Development/git-workshop.git
```

---

### Creating your branch:
3. Now we are going to create a branch specifically for you to work on. There are two types of branches that we can use

| Local | Remote |
| --- | --- |
| Stored on your computer | Stored on Github |

- Today we will be creating a local branch and publishing it onto the workshop repository

We can create our branch a couple different ways:

<details>
<summary> Using Git Checkout</summary>
git checkout -b [INSERT YOUR BRANCH NAME]
</details>

<details>
<summary> Using Git Branch</summary>
git branch [INSERT YOUR BRANCH NAME]

git checkout [INSERT YOUR BRANCH NAME]
</details>

---

### Pushing your changes:
4. We want to make sure we are currently on our new branch. 
- Make sure to use <code style="color:#A9FFF7">git branch</code> to view the branch you are on. 
- You can switch to your branch by using "<code style="color:#A9FFF7">git checkout [INSERT YOUR BRANCH NAME]</code>"

  Steps:
  1. Change line 144 in your index.html to your name. 
  2. In your terminal, you want to commit the changes you have made so type the following:
    ```
    git commit -m "[INSERT YOUR MESSAGE HERE]" index.html
    ```
  3. Once this is complete, you've officially made your first commit. 
  4. Then type <code style="color:#A9FFF7">git push</code> into your terminal
---
### Check for everyone else's branches
5. Remember <code style="color:#A9FFF7">git fetch</code>? Now we should be able to see everyone else's branches on the remote repository when we type <code style="color:#A9FFF7">git fetch</code>. 


---
## <code style="color:#6D98BA"> Congrats, you know the basics of committing and pushing to Git!  </code>