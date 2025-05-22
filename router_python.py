import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("routers_yaml.yml") as f:
        data = yaml.safe_load(f)
        # print(data)
        # Load Jinja2 template
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("router_config.j2")

        # Render config
        config = template.render(routers=data["routers"])

        # Save to file
        with open("generated_config.txt", "w") as f:
                f.write(config)


