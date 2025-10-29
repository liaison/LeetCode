class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.curr = 0


    def visit(self, url: str) -> None:
        # reset the forward history
        self.pages = self.pages[:self.curr+1]
        # add the newly-visited page
        self.pages.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.pages[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += min(steps, len(self.pages) - self.curr - 1)
        return self.pages[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)