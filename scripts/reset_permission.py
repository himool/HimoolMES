from apps.system.models import Team, PermissionGroup, Permission
import itertools


PERMISSIONS = [
    {
        'name': '基础数据',
        'permissions': [
            {'name': '客户分类查询', 'code': 'client_category.get'},
            {'name': '客户分类创建', 'code': 'client_category.post'},
            {'name': '客户分类编辑', 'code': 'client_category.put'},
            {'name': '客户分类删除', 'code': 'client_category.delete'},
            {'name': '客户查询', 'code': 'client.get'},
            {'name': '客户创建', 'code': 'client.post'},
            {'name': '客户编辑', 'code': 'client.put'},
            {'name': '客户删除', 'code': 'client.delete'},
            {'name': '供应商分类查询', 'code': 'supplier_category.get'},
            {'name': '供应商分类创建', 'code': 'supplier_category.post'},
            {'name': '供应商分类编辑', 'code': 'supplier_category.put'},
            {'name': '供应商分类删除', 'code': 'supplier_category.delete'},
            {'name': '供应商查询', 'code': 'supplier.get'},
            {'name': '供应商创建', 'code': 'supplier.post'},
            {'name': '供应商编辑', 'code': 'supplier.put'},
            {'name': '供应商删除', 'code': 'supplier.delete'},
            {'name': '账户查询', 'code': 'account.get'},
            {'name': '账户创建', 'code': 'account.post'},
            {'name': '账户编辑', 'code': 'account.put'},
            {'name': '账户删除', 'code': 'account.delete'},
            {'name': '产品分类查询', 'code': 'product_category.get'},
            {'name': '产品分类创建', 'code': 'product_category.post'},
            {'name': '产品分类编辑', 'code': 'product_category.put'},
            {'name': '产品分类删除', 'code': 'product_category.delete'},
            {'name': '品牌查询', 'code': 'brand.get'},
            {'name': '品牌创建', 'code': 'brand.post'},
            {'name': '品牌编辑', 'code': 'brand.put'},
            {'name': '品牌删除', 'code': 'brand.delete'},
            {'name': '收支分类查询', 'code': 'charge_category.get'},
            {'name': '收支分类创建', 'code': 'charge_category.post'},
            {'name': '收支分类编辑', 'code': 'charge_category.put'},
            {'name': '收支分类删除', 'code': 'charge_category.delete'},
            {'name': '单位查询', 'code': 'unit.get'},
            {'name': '单位创建', 'code': 'unit.post'},
            {'name': '单位编辑', 'code': 'unit.put'},
            {'name': '单位删除', 'code': 'unit.delete'},
        ],
    },
    {
        'name': '产品管理',
        'permissions': [
            {'name': '产品查询', 'code': 'product.get'},
            {'name': '产品创建', 'code': 'product.post'},
            {'name': '产品编辑', 'code': 'product.put'},
            {'name': '产品删除', 'code': 'product.delete'},
            {'name': '批次查询', 'code': 'batch.get'},
            {'name': '批次编辑', 'code': 'batch.get'},
            {'name': '批次删除', 'code': 'batch.get'},
            {'name': '库存查询', 'code': 'inventory.get'},
            {'name': '产品售价查看', 'code': 'product_price.get'},
            {'name': '产品售价调整', 'code': 'inventory.change_price'},
            {'name': '产品上架', 'code': 'inventory.put_on_shelves'},
            {'name': '产品下架', 'code': 'inventory.pull_off_shelves'},
        ],
    },
]


def run(*args):
    PermissionGroup.objects.all().delete()

    for team, permission_group_item in itertools.product(Team.objects.all(), PERMISSIONS):
        permission_group = PermissionGroup.objects.create(name=permission_group_item['name'], team=team)
        Permission.objects.bulk_create([Permission(group=permission_group, name=item['name'], code=item['code'], team=team)
                                        for item in permission_group_item['permissions']])
