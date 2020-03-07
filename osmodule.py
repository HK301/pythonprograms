import os
# basename function
out = os.path.basename("/baz/foo")
print(out)

#directory name function
out = os.path.dirname("/baz/foo")
print(out)


# isabs function
out = os.path.isabs("/baz/foo")
print(out)

# isdirectory function
out = os.path.isdir("C:\\Users")
print(out)

# normcase function for windows
out = os.path.normcase("/BAz")
print(out)
