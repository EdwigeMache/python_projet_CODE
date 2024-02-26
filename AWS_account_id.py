
# using the "find()" method to determined the acount_id
arn= "arn:aws:iam::123456189012:user/Development/product_1234/*"
#start_indix begins after "iam::"
start_index = arn.find("iam::") +5
# The end index closes the end of the count
end_index = arn.find(":user")
#Extfact the account ID using the identified indices
account_id = arn[start_index:end_index]

print(f" the aws account id is:{account_id}")