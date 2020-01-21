from report_manipulator.index_maker import IndexMaker


if __name__ == '__main__':
    index_maker = IndexMaker('../examples/test')
    index_maker.generate_contents()
