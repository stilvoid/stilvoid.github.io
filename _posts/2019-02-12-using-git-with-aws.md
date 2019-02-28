---
tags: git aws
title: Using Git with AWS CodeCommit Across Multiple AWS Accounts
---

(Cross-posted from [the AWS DevOps blog](https://aws.amazon.com/blogs/devops/))

I use [AWS CodeCommit](https://aws.amazon.com/codecommit/) to host all of my private Git repositories. My repositories are split across several AWS accounts for different purposes: personal projects, internal projects at work, and customer projects.

The [CodeCommit documentation](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html) shows you how to configure and clone a repository from one place, but in this blog post I want to share how I manage my Git configuration across multiple AWS accounts.

## Background

First, I have [profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html) configured for each of my AWS environments. I connect to some of them using [IAM user credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) and others by using [cross-account roles](https://aws.amazon.com/blogs/security/how-to-use-a-single-iam-user-to-easily-access-all-your-accounts-by-using-the-aws-cli/).

I intentionally do not have any credentials associated with the default profile. That way I must always be sure I have selected a profile before I run any AWS CLI commands.

Here’s an anonymized copy of my `~/.aws/config` file:

``` config
[profile personal]
region = eu-west-1
aws_access_key_id = ABCDEFGHIJKLMNOPQRST
aws_secret_access_key = uvwxyz0123456789abcdefghijklmnopqrstuvwx

[profile work]
region = us-east-1
aws_access_key_id = ABCDEFGHIJKLMNOPQRST
aws_secret_access_key = uvwxyz0123456789abcdefghijklmnopqrstuvwx

[profile customer]
region = eu-west-2
source_profile = work
role_arn = arn:aws:iam::123456789012:role/CrossAccountPowerUser
```

If I am doing some work in one of those accounts, I run `export AWS_PROFILE=work` and use the AWS CLI as normal.

## The problem

I use the [Git credential helper](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html) so that the Git client works seamlessly with CodeCommit. However, because I use different profiles for different repositories, my use case is a little more complex than the average.

In general, to use the credential helper, all you need to do is place the following options into your `~/.gitconfig` file, like this:

``` config
[credential]
    helper = !aws codecommit credential-helper $@
    UserHttpPath = true
```

I could make this work across accounts by setting the appropriate value for `AWS_PROFILE` before I use Git in a repository, but there is a much neater way to deal with this situation using a feature released in [Git version 2.13](https://blog.github.com/2017-05-10-git-2-13-has-been-released/), [conditional includes](https://git-scm.com/docs/git-config#_includes).

## A solution

First, I separate my work into different folders. My `~/code/` directory looks like this:

``` console
code
    personal
        repo1
        repo2
    work
        repo3
        repo4
    customer
        repo5
        repo6
```

Using this layout, each folder that is directly underneath the code folder has different requirements in terms of configuration for use with CodeCommit.

Solving this has two parts; first, I create a `.gitconfig` file in each of the three folder locations. The `.gitconfig` files contain any customization (specifically, configuration for the credential helper) that I want in place while I work on projects in those folders.

For example:

``` config
[user]
    # Use a custom email address
    email = sengledo@amazon.co.uk

[credential]
    # Note the use of the --profile switch
    helper = !aws --profile work codecommit credential-helper $@
    UseHttpPath = true
```

I also make sure to specify the AWS CLI profile to use in the `.gitconfig` file which means that, when I am working in the folder, I don’t need to set `AWS_PROFILE` before I run `git push`, etc.

Secondly, to make use of these folder-level .gitconfig files, I need to reference them in my global Git configuration at `~/.gitconfig`

This is done through the `includeIf` section. For example:

``` config
[includeIf "gitdir:~/code/personal/"]
    path = ~/code/personal/.gitconfig
```

This example specifies that if I am working with a Git repository that is located anywhere under `~/code/personal/`, Git should load additional configuration from `~/code/personal/.gitconfig`. That additional file specifies the appropriate credential helper invocation with the corresponding AWS CLI profile selected as detailed earlier.

The contents of the new file are treated as if they are inserted into the main `.gitconfig` file at the location of the `includeIf` section.  This means that the included configuration will only override any configuration specified *earlier* in the config.
