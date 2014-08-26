from domain.container import container
import faker


def create_fixtures():
    print 'Creating fixtures'

    fake = faker.Faker()
    user_repository = container('models_user_repository')

    for i in range(0, 10):
        user = user_repository.new(email=fake.email())
        user.first_name = fake.first_name()
        user.last_name = fake.last_name()

        user_repository.insert(user)
