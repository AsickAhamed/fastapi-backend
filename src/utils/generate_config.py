from dotenv import dotenv_values

app_config = {
    **dotenv_values(".env.shared"),
    **dotenv_values(".env.secret")
}
