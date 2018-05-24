import argparse
import subprocess
from distutils.version import LooseVersion


parser = argparse.ArgumentParser(description='Push new superset tags to superset-docker.')
parser.add_argument('--superset-dir', type=str, required=True, help="The git directory of superset.")
parser.add_argument('--superset-docker-dir', type=str, required=True, help="The git directory of superset-docker.")

args = parser.parse_args()

subprocess.check_output(['git', '-C', args.superset_dir, 'fetch'])
subprocess.check_output(['git', '-C', args.superset_docker_dir,
    'fetch', '--prune', 'origin', '+refs/tags/*:refs/tags/*'])
subprocess.check_output(['git', '-C', args.superset_docker_dir, 'pull'])

source_tags = filter(lambda x: x and x[0].isdigit(), subprocess.check_output(['git', '-C', args.superset_dir, 'tag']).split("\n"))

target_tags = filter(lambda x: x, subprocess.check_output(['git', '-C', args.superset_docker_dir, 'tag']).split("\n"))
target_tags = ['v'+x for x in target_tags]

new_tags = list(set(source_tags) - set(target_tags))
new_tags.sort(key=LooseVersion)

print source_tags
print 'aaaaaaaaaaaaaaaaaa'
print target_tags

for tag in new_tags:
    new_tag = "v{}".format(tag)
    with open('superset_version', 'wb') as f:
        f.write(new_tag.lstrip('v'))

    print subprocess.check_output(
        ['git', '-C', args.superset_docker_dir, 'add', 'superset_version'])

    print subprocess.check_output(
        ['git', '-C', args.superset_docker_dir, 'commit', '-m', 'Bump to {}'.format(new_tag)])

    print subprocess.check_output(
        ['git', '-C', args.superset_docker_dir, 'push'])

    print subprocess.check_output(
        ['git', '-C', args.superset_docker_dir, 'tag', new_tag])

    print subprocess.check_output(
        ['git', '-C', args.superset_docker_dir, 'push', 'origin', new_tag])
