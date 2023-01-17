# form-filler
A simple tool to help fill online forms.

# Install

To install use form-filler you need python3 and pynput. Checks if python3 is already installed on your system.

``` 
    python3 --version
```

Install pypunt using pip

```
    pip3 install pynput
```

## Usage

## Keys and Namespace

When you are seeking for jobs, for instance, you gonna fill some forms with data like name, email, etc. Fill-form receive keys and auto type text associated with those keys.

| Key   | Value            |
|-------|------------------|
| name  | Francisco Thiago |
| email | professional@gmail.com  |

Some times you want that the same keys has different values. For instance, in a more informal scenario, you would like to usa an abbreviation of your name.

| Key   | Value            |
|-------|------------------|
| name  | Thiago |
| email | personal@gmail.com  |

That way you can store the same key in a different namespace. When no namespace is specified, autofill uses the default namespace.

## Commands

## Adding Keys and Namespaces

You can use the following code to add your keys

```
    python3 form-filler add namespace_name
```

If no namespace is specified, the default namespace will be used. You can use this method to edit a existing key justing passing a new value to the same key. To create a new namespace use the following command.

```
    python3 form-filler create namespace_name
```

## Filling form

First you need to pass the keys you want to use. Use the following commmand if you are using the default namespace.

```
    python3 form-filler -k key1 key2 key3 ...
```

If you want to use a specific namespace use the following command.

```
    python3 form-filler -ns namespace_name -k key1 key2 key3 ...
```

Once you press enter, form-filler will wait the user to press CRTL 1 and, after that, it will type all values associeted with the givens keys. In adition, after each key, the tab will be pressed to change form's focus. Note that is important to select one field of the form before pressing the shortcut. 

## Reserved keys

Thera are reserved keys to help user pass non printable characters.

| Key   | Value            |
|-------|------------------|
| tab  | Tabulation |
| blnk | Empty string|



